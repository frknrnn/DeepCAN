import numpy as np
import cv2
import os
import tensorflow as tf
import os
import random
import numpy as np
import math
from DeepCAN_Labeling_APP.app_functions.unet_model import model_u
import cv2


class AI():
    def aı_initialize(self,dim,model,hdf5):
        self.hdf5 = hdf5
        self.model_path = model
        self.dim =dim


    def splitImage(self,image):
        unet_input_size = 128
        images = []
        im = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
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
        return image_full[0:2448, 0:3264]

    def AI_threshold(self,images):
        IMG_WIDTH = 128
        IMG_HEIGHT = 128
        IMG_CHANNELS = 1

        modelPath = self.model_path
        if self.hdf5==False:
            self.model = tf.keras.models.load_model(modelPath)
        else:
            self.model = model_u()
            self.model.load_weights(modelPath)
        X_test = np.zeros((len(images), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
        n = 0
        for x in images:
            gray = x
            X_test[n] = np.array(gray).reshape((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
            n = n + 1

        preds_test = self.model.predict(X_test, verbose=1)

        result = []
        for i in range(len(preds_test)):
            sample_pred = preds_test[i]
            norm_image = cv2.normalize(sample_pred, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX,
                                           dtype=cv2.CV_32F)
            norm_image = norm_image.astype(np.uint8)
            ret3, threshold = cv2.threshold(norm_image, 191, 255, cv2.THRESH_BINARY)
            result.append(threshold)
        return result

    def findCells(self,image_threshold,orginal_image):
        self.mainImage = orginal_image.copy()
        self.resultImage = orginal_image.copy()
        self.orginalImage = orginal_image.copy()
        self.orginalImageIntensity = cv2.cvtColor(self.orginalImage,cv2.COLOR_BGR2GRAY)
        self.cells  = []
        self.cellsInformation=[]
        contours, hierarchy = cv2.findContours(image_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        for i in contours:
            area = cv2.contourArea(i)
            cell_rectangle = cv2.boundingRect(i)
            if ( area > 50 and area<(self.dim*self.dim)):
                M = cv2.moments(i)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                if (324<=cY and cY<=2124 ):
                    if(382<=cX and cX<=2882):
                        if(cell_rectangle[3]<self.dim and cell_rectangle[2]<self.dim):
                            new_data,information= self.average_intensity_rectangle(i,self.orginalImageIntensity)
                            self.cellsInformation.append(information)
                            deneme1 = np.array(new_data).reshape((self.dim*self.dim,))
                            self.cells.append(deneme1)


        return  self.cells,self.cellsInformation

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
                    new_list[j + height_offset, i + width_offset] = intensity

        dim = (self.dim, self.dim)
        resized = cv2.resize(new_list, dim, interpolation=cv2.INTER_AREA)

        return resized,cell_information


