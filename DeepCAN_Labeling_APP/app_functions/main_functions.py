import sys
from PySide2 import  QtCore,QtGui,QtWidgets
from PySide2.QtWidgets import *
from PySide2 import  QtCore,QtGui,QtWidgets,QtCharts
from PySide2.QtCharts import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap,QImage
from DeepCAN_Labeling_APP.py_ui.ui_main import Ui_MainWindow
from DeepCAN_Labeling_APP.app_functions.loadingPage import loadingPage
from DeepCAN_Labeling_APP.app_functions.AI import AI
import cv2
import os
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self,app):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.initialSetting()
        self.__press_pos = QPoint()
        self.outputFolder=""
        self.imageName=""
        self.saveDataFlag = False
        self.app =app
        self.model_hdf5=False

        def moveWindow(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

        self.ui.frame_titleBar.mouseMoveEvent = moveWindow

        self.ui.pushButton_exit.clicked.connect(self.exitApp)
        self.ui.pushButton_selectImage.clicked.connect(self.selectImage)
        self.ui.pushButton_selectOutputFolder.clicked.connect(self.selectOutputFolder)
        self.ui.pushButton_selectModelFolder.clicked.connect(self.selectModelFolder)

        self.ui.pushButton_start.clicked.connect(self.startAnalysis)
        self.ui.pushButton_live.clicked.connect(self.selectLive)
        self.ui.pushButton_dead.clicked.connect(self.selectDead)
        self.ui.pushButton_null.clicked.connect(self.selectNull)

        self.ui.pushButton_save.clicked.connect(self.saveData)
        self.ui.pushButton_new.clicked.connect(self.newImage)

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def initialSetting(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.label_total.setVisible(False)

    def selectImage(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Image", "/home",
                                               "Image Files (*.png *.jpg *.bmp *.jpeg *.tif *.tiff)")
        head_tail = os.path.split(str(fileName[0]))
        self.imageName = str(head_tail[1]).split('.')[0]
        self.ui.lineEdit_image.setText(str(fileName[0]))
        self.imagePath = str(fileName[0])
        self.main_image = cv2.imread(str(fileName[0]),0)
        self.main_image = cv2.cvtColor(self.main_image,cv2.COLOR_GRAY2BGR)
        self.liveCells=[]
        self.deadCells=[]
        self.clusterCells = []
        self.liveCell_count=0
        self.deadCell_count=0
        self.viability=0
        self.index=0


    def selectOutputFolder(self):
        outputDir = QFileDialog.getExistingDirectory(
        self,
        "Open a folder",
        "/home",
        QFileDialog.ShowDirsOnly
        )
        self.ui.lineEdit_outputFolder.setText(str(outputDir))
        self.outputFolder = str(outputDir)

    def selectModelFolder(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Model", "/home",
                                               "Model Files (*.h5 *.hdf5)")
        self.ui.lineEdit_modelFolder.setText(str(fileName[0]))
        self.modelPath = str(fileName[0])
        file,extension =os.path.splitext(fileName[0])
        if(extension==".hdf5"):
            self.model_hdf5=True
        else:
            self.model_hdf5=False

    def startAnalysis(self):
        self.dim = int(self.ui.comboBox.currentText())
        folderControlFlag = self.folderControl()
        if (folderControlFlag):
            self.loadPage = loadingPage()
            self.ai_count = AI()
            self.ai_count.aı_initialize(self.dim,self.modelPath,self.model_hdf5)
            self.ui.stackedWidget.setCurrentIndex(2)
            self.timer_aı = QTimer()
            self.timer_aı.timeout.connect(self.startClusterSplit)
            self.timer_aı.start(100)
        else:
            pass


    def startClusterSplit(self):
        split_image = self.ai_count.splitImage(self.main_image)
        threshold_split_images = self.ai_count.AI_threshold(split_image)
        new_image = self.ai_count.merge_image(threshold_split_images)
        self.cellList,self.cellsInformation = self.ai_count.findCells(new_image, self.main_image)
        self.showCell(self.index)
        self.ui.label_totalCell.setText("Total : " +str(len(self.cellList)))
        self.ui.stackedWidget.setCurrentIndex(1)

        self.ui.label_total.setVisible(True)
        self.loadPage.close()
        self.timer_aı.stop()


    def showCell(self,index):
        if(index<len(self.cellList)):

            image = np.array(self.cellList[index]).reshape((self.dim,self.dim))
            #cv2.imwrite("deneme.tif", image)
            self.ui.label_total.setText(str(index)+" / " + str(len(self.cellList)))
            self.ui.label_average.setText("Average : "+str(int(np.mean(self.cellsInformation[index]))))
            self.ui.label_std.setText("STD :" +str(int(np.std(self.cellsInformation[index]))))
            result_image = self.convert_nparray_to_QPixmap(np.array(image).astype(dtype='uint8'))
            #pixmap = QPixmap('deneme.tif')
            resized_pixmap = result_image.scaled(self.ui.pictureBox.width(), self.ui.pictureBox.height(),
                                            QtCore.Qt.KeepAspectRatio)
            self.ui.pictureBox.setPixmap(resized_pixmap)
            self.ui.label_liveCell.setText("Live :"+" "+str(self.liveCell_count))
            self.ui.label_deadCell.setText("Dead :"+" "+str(self.deadCell_count))
            if(self.liveCell_count!=0 and self.deadCell_count!=0):
                self.ui.label_viability.setText("Viability : "+ str(int((self.liveCell_count/(self.liveCell_count+self.deadCell_count))*100))+" %")
            elif(self.deadCell_count==0):
                self.ui.label_viability.setText("Viability : "+ "100 %")
            else:
                self.ui.label_viability.setText("Viability : "+ "0 %")
        else:
            pass



    def selectLive(self):
        if (self.index < len(self.cellList)):
            self.liveCells.append(np.array(self.cellList[self.index]).reshape((self.dim*self.dim,)))
            self.liveCell_count=self.liveCell_count+1
            self.ui.listWidget_Live.addItem(str(self.index))
            self.index=self.index+1
            self.showCell(self.index)
        else:
            self.ui.pushButton_live.setEnabled(False)
            self.ui.pushButton_dead.setEnabled(False)
            self.ui.pushButton_null.setEnabled(False)

    def selectDead(self):
        if (self.index < len(self.cellList)):
            self.deadCells.append(np.array(self.cellList[self.index]).reshape((self.dim*self.dim,)))
            self.deadCell_count = self.deadCell_count + 1
            self.ui.listWidget_dead.addItem(str(self.index))

            self.index = self.index + 1
            self.showCell(self.index)
        else:
            self.ui.pushButton_live.setEnabled(False)
            self.ui.pushButton_dead.setEnabled(False)
            self.ui.pushButton_null.setEnabled(False)

    def selectNull(self):
        if (self.index < len(self.cellList)):
            self.clusterCells.append(np.array(self.cellList[self.index]).reshape((self.dim * self.dim,)))
            self.index = self.index + 1
            self.showCell(self.index)
        else:
            self.ui.pushButton_live.setEnabled(False)
            self.ui.pushButton_dead.setEnabled(False)
            self.ui.pushButton_null.setEnabled(False)


    def convert_nparray_to_QPixmap(self, img):
        w, h = img.shape
        bytesPerLine = w
        qImg = QImage(img, w, h, bytesPerLine, QImage.Format_Grayscale8)
        qpixmap = QPixmap(qImg)
        resizde_pixmap = qpixmap.scaled(self.ui.pictureBox.width(), self.ui.pictureBox.height(), QtCore.Qt.KeepAspectRatio)
        return resizde_pixmap


    def saveData(self):
        self.saveDataFlag=True
        np.savetxt(self.outputFolder+"/"+self.imageName+"_live.csv", self.liveCells, delimiter=",")
        np.savetxt(self.outputFolder+"/"+self.imageName+"_dead.csv", self.deadCells, delimiter=",")
        np.savetxt(self.outputFolder+"/"+self.imageName+"_cluster.csv", self.clusterCells, delimiter=",")


    def folderControl(self):
        if(len(self.ui.lineEdit_outputFolder.text())==0 or len(self.ui.lineEdit_image.text())==0 or len(self.ui.lineEdit_modelFolder.text())==0):
            return False
        else:
            return True

    def newImage(self):
        if(self.saveDataFlag):
            self.ui.label_total.setVisible(False)
            self.ui.lineEdit_image.clear()
            self.ui.lineEdit_outputFolder.clear()
            self.ui.listWidget_dead.clear()
            self.ui.listWidget_Live.clear()
            self.ui.stackedWidget.setCurrentIndex(0)
            self.saveDataFlag=False
            self.ui.pushButton_live.setEnabled(True)
            self.ui.pushButton_dead.setEnabled(True)
            self.ui.pushButton_null.setEnabled(True)
        else:
            pass



    def exitApp(self):
        sys.exit(self.app.exec_())
        exit(0)