import numpy as np
import cv2
import os
import tensorflow as tf
import os
import random
import numpy as np
import math
from vgg16_unet_model import build_vgg16_unet
import matplotlib.pyplot as plt
class AI_count():
    def setParameters(self,deviceCalibration,size):
        self.calibrationValue = deviceCalibration
        self.dim = size

    def setModelPath_h5(self,unet,cnn,output,threshold):
        self.unetPath = unet
        self.viabilityPath = cnn
        self.model_unet = tf.keras.models.load_model(unet)
        self.threshold =threshold

    def setModelPath_hdf5(self,unet,cnn,output,cluster_cnn,threshold):
        self.unet_output=output
        self.threshold=threshold
        self.unetPath = unet
        self.model_unet = build_vgg16_unet((128,128,3))
        self.model_unet.load_weights(unet)
        self.viabilityPath = cnn
        self.clusterPath = cluster_cnn

    def crop_image(self,im, unet_input_size, shift_x, shift_y):
        size_im = im.shape
        im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        pad_size_x, pad_size_y = 0, 0
        if size_im[0] % unet_input_size != 0:
            pad_size_y = (size_im[0] // unet_input_size + 1) * unet_input_size - size_im[0]
        if size_im[1] % unet_input_size != 0:
            pad_size_x = (size_im[1] // unet_input_size + 1) * unet_input_size - size_im[1]

        pad_im = np.pad(im, ((shift_y, pad_size_y + shift_y), (shift_x, pad_size_x + shift_x)),
                        mode='mean')  # )mode='constant',constant_values=0
        size_pad_im = pad_im.shape
        x_div, y_div = np.int64(size_pad_im[1] / unet_input_size), np.int64(size_pad_im[0] / unet_input_size)

        im_cropped = []
        count = 0
        for j in range(y_div):
            for i in range(x_div):
                cropped = pad_im[j * unet_input_size:(j + 1) * unet_input_size,
                          i * unet_input_size:(i + 1) * unet_input_size]
                im_cropped.append(np.uint8(cropped))
                count = count + 1

        return im_cropped

    def merge_image2(self,images, cr_sizeX, cr_sizeY, fullResX, fullResY, shift_x, shift_y):
        v_images = []
        y_scan = fullResY // cr_sizeY + 1
        x_scan = fullResX // cr_sizeX + 1
        for i in range(y_scan):
            v_img = cv2.hconcat(images[(i * x_scan):((i * x_scan) + x_scan)])
            v_images.append(v_img)
        image_full = cv2.vconcat(v_images)
        return image_full[shift_y:fullResY + shift_y, shift_x:fullResX + shift_x]


    def splitImage(self,image):
        unet_input_size = 128
        images = []
        #im = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        im=image
        size_im = im.shape
        pad_size_x, pad_size_y = 0, 0
        if size_im[0] % unet_input_size != 0:
            pad_size_y = (size_im[0] // unet_input_size + 1) * unet_input_size - size_im[0]
        if size_im[1] % unet_input_size != 0:
            pad_size_x = (size_im[1] // unet_input_size + 1) * unet_input_size - size_im[1]
        pad_im = np.pad(im, ((0, pad_size_y), (0, pad_size_x)), mode='mean')
        del im
        size_pad_im = pad_im.shape
        x_div, y_div = np.int64(size_pad_im[1] / unet_input_size), np.int64(size_pad_im[0] / unet_input_size)
        for j in range(y_div):
            for i in range(x_div):
                cropped = pad_im[j * unet_input_size:(j + 1) * unet_input_size,
                          i * unet_input_size:(i + 1) * unet_input_size]
                images.append(cropped)
        return images

    def merge_image(self,images):
        v_images = []
        for i in range(20):
            v_img = cv2.hconcat(images[(i * 26):((i * 26) + 26)])
            v_images.append(v_img)
        image_full = cv2.vconcat(v_images)
        cv2.imwrite(self.unet_output,image_full[0:2448, 0:3264])
        return image_full[0:2448, 0:3264]

    def AI_threshold(self,images):
        IMG_WIDTH = 128
        IMG_HEIGHT = 128
        IMG_CHANNELS = 3
        X_test = np.zeros((len(images), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
        n = 0
        for x in images:
            gray = x
            gray = np.stack((gray,) * 3, axis=-1)
            X_test[n] = np.array(gray).reshape((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
            n = n + 1
        preds_test = self.model_unet.predict(X_test, verbose=1)

        result = []
        for i in range(len(preds_test)):
            sample_pred = preds_test[i]
            norm_image = cv2.normalize(sample_pred, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX,
                                           dtype=cv2.CV_32F)
            norm_image = norm_image.astype(np.uint8)
            ret3, threshold = cv2.threshold(norm_image, self.threshold, 255, cv2.THRESH_BINARY)
            result.append(threshold)
        return result

    def findCells(self,image_threshold,orginal_image,viability):
        self.mainImage = orginal_image.copy()
        self.resultImage = orginal_image.copy()
        self.orginalImage = orginal_image.copy()
        self.orginalImageIntensity=orginal_image.copy()
        self.orginalImageIntensity = cv2.cvtColor(self.orginalImage,cv2.COLOR_BGR2GRAY)

        self.cluster_model = tf.keras.models.load_model(self.clusterPath)
        if(viability):
            self.viability_model = tf.keras.models.load_model(self.viabilityPath)

        self.liveCellDiameter  = []
        self.deadCellDiameter  = []
        self.totalCellDiameter = []
        self.liveCellContour   = []
        self.deadCellContour   = []
        self.totalCellContour  = []
        self.centers = []
        self.new_contours = []
        self.cluster_contours = []
        self.clusterCells = []
        self.temp = []
        contours, hierarchy = cv2.findContours(image_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for i in contours:
            area = cv2.contourArea(i)
            r = int(math.sqrt(area / math.pi))
            diameter = r * 2 * self.calibrationValue
            if ( area > 50 and area<2500):
                M = cv2.moments(i)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                if (324 <= cY and cY <= 2124):
                    if (382 <= cX and cX <= 2882):
                        isClusterData, cell_information = self.average_intensity_rectangle(i, self.orginalImageIntensity)
                        isClusterData = np.array(isClusterData).reshape(1, self.dim, self.dim, 1)
                        a = isClusterData
                        isClusterData = isClusterData / 255
                        cluster_predictions = self.cluster_model.predict(isClusterData)
                        cluster_result = np.argmax(cluster_predictions, axis=1)
                        if(cluster_result==1):
                            self.centers.append((cX, cY))
                            self.new_contours.append(i)
                            viability_data = isClusterData
                            if (viability):
                                predictions = self.viability_model.predict(viability_data)
                                classes = np.argmax(predictions, axis=1)
                            else:
                                classes = 1
                            if (classes == 1):
                                self.totalCellContour.append(i)
                                self.totalCellDiameter.append(diameter)
                                self.liveCellDiameter.append(diameter)
                                self.liveCellContour.append(i)
                                cv2.drawContours(self.resultImage, i, -1, (0, 255, 0), 3)
                            else:
                                cv2.drawContours(self.resultImage, i, -1, (0, 0, 255), 3)
                                self.totalCellContour.append(i)
                                self.totalCellDiameter.append(diameter)
                                self.deadCellDiameter.append(diameter)
                                self.deadCellContour.append(i)

                        else:
                            cv2.drawContours(self.resultImage, i, -1, (0, 255, 255), 4)
                            self.cluster_contours.append(i)
                            self.temp.append(a)
        #################### FİND CELLS IN CLUSTERS ###################
        #print("Cluster Count")
        #print(np.array(self.temp).shape)
        #### Preprocessing ###
        self.gray_image = orginal_image.copy()
        self.gray_image = cv2.cvtColor(self.gray_image, cv2.COLOR_BGR2GRAY)

        #self.gray_image = cv2.medianBlur(self.gray_image, 5)
        #cv2.imwrite("circle.png",self.gray_image)
        circles = cv2.HoughCircles(self.gray_image, cv2.HOUGH_GRADIENT, 1, 11,
                                  param1=110, param2=10,
                                  minRadius=5, maxRadius=13)

        #print("circle"+str(len(circles)))

        #print(np.array(circles).shape)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                for j in self.cluster_contours:
                    dist = cv2.pointPolygonTest(j,center, False)
                    if(dist>=0):
                        self.centers.append(center)
                        result,cc = self.circle_intensity_rectangle(self.orginalImageIntensity,j,center,i[2])
                        self.clusterCells.append(np.array(result).reshape(2500))
                        result = np.array(result).reshape(1, self.dim, self.dim, 1)
                        result = result / 255

                        if (viability):
                            viability_predictions = self.viability_model.predict(result)
                            viability_result = np.argmax(viability_predictions, axis=1)
                        else:
                            viability_result = 1
                        if (viability_result == 1):
                            self.totalCellContour.append(i)
                            self.totalCellDiameter.append(diameter)
                            self.liveCellDiameter.append(diameter)
                            self.liveCellContour.append(i)
                            cv2.circle(self.resultImage, center, 1, (255, 0, 0), 3)
                            cv2.circle(self.resultImage, center, i[2], (0, 255, 0), 3)

                        else:

                            self.totalCellContour.append(i)
                            self.totalCellDiameter.append(diameter)
                            self.deadCellDiameter.append(diameter)
                            self.deadCellContour.append(i)
                            cv2.circle(self.resultImage, center, 1, (255, 0, 0), 3)
                            cv2.circle(self.resultImage, center, i[2], (0, 0, 255), 3)

        cv2.line(self.resultImage,(382,324),(382,2124),(0,0,0),2)
        cv2.line(self.resultImage,(2882,324),(2882,2124),(0,0,0),2)
        cv2.line(self.resultImage,(382,324),(2882,324),(0,0,0),2)
        cv2.line(self.resultImage,(382,2124),(2882,2124),(0,0,0),2)
        #np.savetxt("orginal_cluster.csv", self.clusterCells, delimiter=",")
        return  self.resultImage


    def copy_image_toList(self,contour, img):
        cell_rectangle = cv2.boundingRect(contour)
        all_intensity = []
        for i in range(cell_rectangle[3]):
            for j in range(cell_rectangle[2]):
                X = cell_rectangle[0] + j
                Y = cell_rectangle[1] + i
                intensity = img[Y, X]
                all_intensity.append(intensity)
        dim = (self.dim, self.dim)
        all_intensity = np.array(all_intensity).reshape((cell_rectangle[3], cell_rectangle[2]))
        resized = cv2.resize(all_intensity, dim, interpolation=cv2.INTER_AREA)
        return resized

    def average_intensity_rectangle(self,contour,img):
        cell_rectangle = cv2.boundingRect(contour)
        new_list = []
        cell_information=[]
        for i in range(self.dim*self.dim):
            new_list.append(0)
        new_list=np.array(new_list).reshape((self.dim,self.dim))
        width_offset = int((self.dim - cell_rectangle[3]) / 2)
        height_offset = int((self.dim - cell_rectangle[2]) / 2)
        for i in range(cell_rectangle[3]):
            for j in range(cell_rectangle[2]):
                X = cell_rectangle[0] + j
                Y = cell_rectangle[1] + i
                dist = cv2.pointPolygonTest(contour, (X, Y), False)
                if (dist >= 0):
                    intensity = img[Y, X]
                    cell_information.append(intensity)
                    if(j+height_offset<50 and (i+width_offset)<50):
                        new_list[j + height_offset, i + width_offset] = intensity

        dim = (self.dim, self.dim)
        resized = cv2.resize(new_list, dim, interpolation=cv2.INTER_AREA)

        return resized,cell_information

    def circle_intensity_rectangle(self,img,contour,center,radius):
        new_list = []
        cell_information = []
        for i in range(self.dim * self.dim):
            new_list.append(0)
        new_list = np.array(new_list).reshape((self.dim, self.dim))
        width_offset = int((self.dim - (radius*2.5))/2)
        height_offset = int((self.dim - (radius*2.5))/2)
        for i in range(int(radius*2.5)):
            for j in range(int(radius*2.5)):
                X = center[0]-int(radius) + j
                Y = center[1]-int(radius) + i
                dist = cv2.pointPolygonTest(contour, (X, Y), False)
                if (dist >= 0):
                    intensity = img[Y, X]
                    cell_information.append(intensity)
                    if(j+height_offset<50 and (i+width_offset)<50):
                        new_list[j + height_offset, i + width_offset] = intensity

        dim = (self.dim, self.dim)
        resized = cv2.resize(new_list, dim, interpolation=cv2.INTER_AREA)

        return resized,cell_information





    def calculateViabilityPercent(self):
        if(len(self.liveCellDiameter)>0 and len(self.totalCellDiameter)>0):
            self.livePercent = (len(self.liveCellDiameter)/len(self.totalCellDiameter))*100
        else:
            self.livePercent = 0

        if (len(self.deadCellDiameter) > 0 and len(self.totalCellDiameter) > 0):
            self.deadPercent = (len(self.deadCellDiameter) / len(self.totalCellDiameter)) * 100
        else:
            self.deadPercent = 0

        return self.livePercent,self.deadPercent

    def showTotalCells(self, min, max):
        resultImage = self.mainImage.copy()
        for i in range(len(self.liveCellContour)):
            if(min<=self.liveCellDiameter[i] and max>=self.liveCellDiameter[i]):
                cv2.drawContours(resultImage, self.liveCellContour[i], -1, (0, 255, 0), 3)
        for i in range(len(self.deadCellContour)):
            if(min<=self.deadCellDiameter[i] and max>=self.deadCellDiameter[i]):
                cv2.drawContours(resultImage, self.deadCellContour[i], -1, (0, 0, 255), 3)
        return resultImage

    def showLiveCells(self, min, max):
        resultImage = self.mainImage.copy()
        for i in range(len(self.liveCellContour)):
            if (min <= self.liveCellDiameter[i] and max >= self.liveCellDiameter[i]):
                cv2.drawContours(resultImage, self.liveCellContour[i], -1, (0, 255, 0), 3)
        return resultImage

    def showDeadCells(self, min, max):
        resultImage = self.mainImage.copy()
        for i in range(len(self.deadCellContour)):
            if(min<=self.deadCellDiameter[i] and max>=self.deadCellDiameter[i]):
                cv2.drawContours(resultImage, self.deadCellContour[i], -1, (0, 0, 255), 3)
        return resultImage

    def calculateAverageDiameter(self,type,min,max):
        #type=1 total 2 live 3 dead
        size = 0
        total_diameter = 0
        liveCellSize=0
        deadCellSize=0
        if(type==1 or type==2):
            for i in range(len(self.liveCellContour)):
                if (min <= self.liveCellDiameter[i] and max >= self.liveCellDiameter[i]):
                    size=size+1
                    total_diameter=total_diameter+self.liveCellDiameter[i]
                    liveCellSize = liveCellSize+1
        if(type==1 or type==3):
            for i in range(len(self.deadCellContour)):
                if (min <= self.deadCellDiameter[i] and max >= self.deadCellDiameter[i]):
                    size=size+1
                    total_diameter=total_diameter+self.deadCellDiameter[i]
                    deadCellSize = deadCellSize + 1

        if(size==0):
            size=1
        average_diameter = total_diameter/size
        live_viability = (liveCellSize / size) * 100
        dead_viability = (deadCellSize / size) * 100

        return average_diameter,size,liveCellSize,deadCellSize,live_viability,dead_viability
    def getParameters(self):
        return self.totalCellDiameter,self.totalCellContour,self.liveCellDiameter,self.liveCellContour,self.deadCellDiameter,self.deadCellContour

    def distanceMetric(self,gt):
        groundTruth = cv2.imread(gt, 0)
        copy_groundTruth = groundTruth.copy()
        copy_groundTruth = cv2.cvtColor(copy_groundTruth, cv2.COLOR_GRAY2BGR)
        g_contours, _ = cv2.findContours(groundTruth, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        distances = []
        count = 0
        fn_=0
        for i in range(len(self.centers)):
            flag2=False
            for j in range(len(g_contours)):
                M = cv2.moments(g_contours[j])
                if(M["m00"]==0):
                    M["m00"]=1
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                if (324 <= cY and cY <= 2124):
                    if (382 <= cX and cX <= 2882):
                        flag = cv2.pointPolygonTest(g_contours[j], self.centers[i], False)
                        if flag == 1:
                            count = count + 1
                            flag2 = True
                            value = math.dist(self.centers[i], (cX, cY))
                            cv2.circle(copy_groundTruth, (cX, cY), 1, (0, 255, 0), 4)
                            distances.append(value)

                            g_contours = np.delete(g_contours, j, 0)
                            break
            if flag2==False:
                fn_=fn_+1
                cv2.circle(copy_groundTruth, self.centers[i], 1,(255, 0, 0), 4)


        #print("FN ")
        Fp_count = 0
        for i in range(len(g_contours)):
            M = cv2.moments(g_contours[i])
            if (M["m00"] == 0):
                M["m00"] = 1
            cX2 = int(M["m10"] / M["m00"])
            cY2 = int(M["m01"] / M["m00"])
            if (324 <= cY2 and cY2 <= 2124):
                if (382 <= cX2 and cX2 <= 2882):
                    cv2.circle(copy_groundTruth, (cX2, cY2), 1, (0, 0, 255), 4)
                    Fp_count=Fp_count+1

        #print(Fp_count)
        #print("TP")
        #print(count)
        #print("FP")
        #print(len(self.centers)-count)
        #print("distances average")
        #print(sum(distances) / len(distances))
        ''''
        a = self.splitImage(copy_groundTruth)

        b = self.ind_corner(a)

        c = self.merge_image2(b)
        '''
        cv2.imwrite("rr.png", copy_groundTruth)

        #print(np.array(self.centers).shape)
        #print(fn_)

    def ind_corner(self,images):
        im_shape = images[0].shape
        rgb_images = []
        for i in range(len(images)):
            if len(images[i].shape) == 2:
                cropped = cv2.cvtColor((images[i]), cv2.COLOR_GRAY2BGR)
            else:
                cropped = images[i]
            cropped[0:im_shape[0], 0] = (255, 0, 0)
            cropped[im_shape[0] - 1, 0:im_shape[1]] = (255, 0, 0)
            cropped[0:im_shape[0], im_shape[1] - 1] = (255, 0, 0)
            cropped[0, 0:im_shape[1]] = (255, 0, 0)
            rgb_images.append(cropped)
        return rgb_images