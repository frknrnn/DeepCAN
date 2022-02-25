import tensorflow as tf
import os
import random
import numpy as np

import matplotlib.pyplot as plt
import cv2
from matplotlib import pyplot
import time
from tensorflow.keras import backend as K
from matplotlib import pyplot as plt
from model import build_vgg16_unet
import math

t1=time.time()
# GPU
physical_devices = tf.config.list_physical_devices('GPU')
config = tf.config.experimental
config.set_memory_growth(physical_devices[0], True)

def flipImage(image):
    image1 = image.copy()
    image2 = image.copy()
    image3 = image.copy()
    images = []
    image1 = cv2.flip(image1,-1)
    image2 = cv2.flip(image2,0)
    image3 = cv2.flip(image3,1)
    images.append(image)
    images.append(image1)
    images.append(image2)
    images.append(image3)
    return images


IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_CHANNELS = 3
dataAugmentation = True


orginalPath = 'Data/orginal_crop'
labelPath = 'UnetData/label_crop'

orginalFolder = os.listdir(orginalPath)
labelFolder = os.listdir(labelPath)

if(dataAugmentation):
    sampleSize = len(orginalFolder)*4
else:
    sampleSize = len(orginalFolder)

X_train = np.zeros((sampleSize, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)

print(sampleSize)
Y_train = np.zeros((sampleSize, IMG_HEIGHT, IMG_WIDTH, 1), dtype=np.uint8)
pixel_weights = np.zeros((sampleSize, IMG_HEIGHT, IMG_WIDTH, 1))
n=0
for x in orginalFolder:
    gray = cv2.imread(orginalPath+"/"+x,0)
    gray = np.stack((gray,) * 3, axis=-1)
    if(dataAugmentation):
        datas = flipImage(gray)
        for i in datas:
            X_train[n]=np.array(i).reshape((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
            n=n+1
    else:
        X_train[n]=np.array(gray).reshape((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
        n=n+1

n=0

white_pixel = 0
black_pixel = 0
total_cell_count = 0

for x in labelFolder:
    gray = cv2.imread(labelPath+"/"+x,0)
    ret,gray_threshold = cv2.threshold(gray,150,1,cv2.THRESH_BINARY)
    ret, gray_= cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    contours= cv2.findContours(gray_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total_cell_count=total_cell_count+len(contours)

    white_pixel = white_pixel+np.sum(gray_threshold)
    black_pixel = black_pixel+((128*128)-np.sum(gray_threshold))
    if(dataAugmentation):
        datas = flipImage(gray_threshold)
        for i in datas:
            Y_train[n]=np.array(i).reshape((IMG_HEIGHT, IMG_WIDTH,1))
            n=n+1
    else:
        Y_train[n]=np.array(gray_threshold).reshape((IMG_HEIGHT, IMG_WIDTH,1))
        n=n+1
print(total_cell_count)

train_masks_reshaped = Y_train.reshape((len(Y_train) * (128 * 128),))

# Build the model
input_shape = (128, 128,3)
model = build_vgg16_unet(input_shape)
model.summary()

model.compile(loss = tf.keras.losses.BinaryCrossentropy(from_logits=True),optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy',tf.keras.metrics.MeanIoU(num_classes=2)])

results = model.fit(X_train, Y_train, batch_size=16,epochs=5,validation_split=0.2, verbose=2)#, callbacks=callbacks)

#results = model.fit([X_train,Y_train,weights], Y_train, batch_size=128,epochs=14,validation_split=0.1)#, callbacks=callbacks)
print(results.history.keys())

plt.plot(results.history['accuracy'])
plt.plot(results.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

plt.plot(results.history['loss'])
plt.plot(results.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

#model.save_weights('a2780_vgg16_unet_w0.hdf5')

