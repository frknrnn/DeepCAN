import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import cv2
import os
import math
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from model import build_vgg16_unet
import matplotlib.pyplot as plt
from unet_model import model_u


num_channels = 1
img_rows = 128
img_cols = 128
num_classes = 2

X = cv2.imread("test.png",0)

X = np.stack((X,) * 3, axis=-1)
print(X.shape)

X = np.array(X).reshape(1, 2448, 3264, 3)
input_shape = (2448, 3264,3)
model = build_vgg16_unet(input_shape)
model.load_weights("a2780_vgg16_unet_w0.hdf5")



predictions = model.predict(X,verbose=1)

predictions = np.array(predictions).reshape((2448, 3264))
print(predictions.shape)


norm_image = cv2.normalize(predictions, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX,
                                           dtype=cv2.CV_32F)
norm_image = norm_image.astype(np.uint8)
ret3, threshold = cv2.threshold(norm_image, 230, 255, cv2.THRESH_BINARY)


cv2.imwrite("test.png",threshold)

