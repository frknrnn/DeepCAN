from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from getDataSet import dataSet
from lenet_5_model import lenet5
import time

num_channels = 1
img_rows = 50
img_cols = 50
num_classes = 2

cluster_cell_folder_path = "/Cluster_data/Cluster"
single_cell_folder_path = "/Cluster_data/noCluster"
model_path = "DeepCan_test/Model_weights"

data_ = dataSet()

X,Y = data_.getData(cluster_cell_folder_path, single_cell_folder_path)

#print(len(C))

########### VALIDATION SPLİT ################
X_train, X_test, Y_train, Y_test = train_test_split(np.array(X), np.array(Y), test_size=0.20)

################# RESIZE FOR MODEL ###########
X_train /=255
X_test  /=255

X_train=np.array(X_train).reshape((len(X_train),img_rows,img_cols,num_channels))
X_test=np.array(X_test).reshape((len(X_test),img_rows,img_cols,num_channels))

Y_train = np_utils.to_categorical(Y_train, num_classes)
Y_test = np_utils.to_categorical(Y_test, num_classes)


model = lenet5().model(img_rows,img_cols,num_channels)


batchSize=16
epochSize=100
validation_split=0.20

start_time=[]
end_time=[]
Accuracy=[]
for i in range(1):
    start=time.time()
    history = model.fit(X_train, Y_train, batch_size=batchSize,
                        epochs=epochSize, validation_split=validation_split,verbose=2)
    score = model.evaluate(X_test, Y_test,
                          batch_size=batchSize,)
    Accuracy.append(score[1])
    end=time.time()
    start_time.append(start)
    end_time.append(end)

training_loss = history.history['loss']
test_loss = history.history['val_loss']

#model.save(model_path+"/"+'v1_cluster.h5')

################### #############

# Create count of the number of epochs
epoch_count = range(1, len(training_loss) + 1)

# Visualize loss history
plt.axis([0, epochSize, 0, 1])
plt.plot(epoch_count, training_loss, 'r-')
plt.plot(epoch_count, test_loss, 'b-')
plt.legend(['Training Loss', 'Test Loss'],labelsize=20)
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
plt.xlabel('Epoch',labelsize=20)
plt.ylabel('Accuracy',labelsize=20)
plt.show();

