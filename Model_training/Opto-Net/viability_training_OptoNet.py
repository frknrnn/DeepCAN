import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from getDataSet import dataSet
from model import Optonet
from sklearn.utils import class_weight
from keras.utils import np_utils
from sklearn.model_selection import KFold, StratifiedKFold

from tensorflow.keras.preprocessing.image import ImageDataGenerator



num_channels = 1
img_rows = 50
img_cols = 50
num_classes = 2

cluster_folder_path = "/Cluster_data/Cluster"
no_cluster_folder_path = "/Cluster_data/noCluster"
model_path = "DeepCan_test/Model_weights"

data_ = dataSet()

X,Y = data_.getData(cluster_folder_path,no_cluster_folder_path)


########### VALIDATION SPLİT ################
X_train, X_test, Y_train, Y_test = train_test_split(np.array(X), np.array(Y), test_size=0.20)

################# RESIZE FOR MODEL ###########
X_train /=255
X_test  /=255
X_train=np.array(X_train).reshape((len(X_train),img_rows,img_cols,num_channels))
X_test=np.array(X_test).reshape((len(X_test),img_rows,img_cols,num_channels))

class_weights = class_weight.compute_class_weight(class_weight='balanced',classes= np.unique(Y_train),y= Y_train)

Y_train = np_utils.to_categorical(Y_train, num_classes)
Y_test = np_utils.to_categorical(Y_test, num_classes)


idg = ImageDataGenerator(width_shift_range=0.1,
                         height_shift_range=0.1,
                         zoom_range=0.3,
                         fill_mode='nearest',
                         horizontal_flip = True,
                         vertical_flip=True,
                         brightness_range=[0.2,0.8],
                         )

print(class_weights)


model = Optonet().model(img_rows, img_cols, num_channels)


batchSize=2
epochSize=50

history = model.fit_generator(idg.flow(X_train, Y_train, batch_size=batchSize),
                    epochs=epochSize, # one forward/backward pass of training data
                    steps_per_epoch=X_train.shape[0]//batchSize, # number of images comprising of one epoch
                    validation_data=(X_test, Y_test), # data for validation
                    validation_steps=X_test.shape[0]//batchSize,verbose=2)




training_loss = history.history['loss']
test_loss = history.history['val_loss']



################### #############

# Create count of the number of epochs
epoch_count = range(1, len(training_loss) + 1)

# Visualize loss history
plt.axis([0, epochSize, 0, 1])
plt.plot(epoch_count, training_loss, 'r-')
plt.plot(epoch_count, test_loss, 'b-')
plt.legend(['Training Loss', 'Test Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show();
# Get training and test loss histories
training_loss = history.history['accuracy']
test_loss = history.history['val_accuracy']

# Create count of the number of epochs
epoch_count = range(1, len(training_loss) + 1)
# Visualize loss history
plt.axis([0, epochSize, 0, 1])
plt.plot(epoch_count, training_loss, 'r-')
plt.plot(epoch_count, test_loss, 'b-')
plt.legend(['Training accuracy', 'Test accuracy'])
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()


#model.save(model_path+"/"+'v1_viability.h5')



