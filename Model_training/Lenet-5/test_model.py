from getDataSet import dataSet
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
import seaborn as sns
from keras.utils import np_utils
import matplotlib.pyplot as plt

num_channels = 1
img_rows = 50
img_cols = 50
num_classes = 2

cluster_folder_path = "/Cluster_data/Cluster"
no_cluster_folder_path = "/Cluster_data/noCluster"

clusterPath = "/Models_weights/v1_cluster.h5"

data_ = dataSet()

X,Y = data_.getData(cluster_folder_path,no_cluster_folder_path)

Y_test = np_utils.to_categorical(Y, 2)

X = np.array(X).reshape(len(X), 50, 50, 1)
X=X/255

model = load_model(clusterPath)

predictions = model.predict(X)

predicted_classes = np.argmax(predictions, axis=1)

report = classification_report(Y, predicted_classes)
print(report)




y_prediction = []
for i in predictions :
  y_prediction.append(np.argmax(i))
y_test = []
for i in Y:
  y_test.append(np.argmax(i))

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.rc('font', **font)

cm = confusion_matrix(Y, predicted_classes)
index = ['Cluster','No Cluster']
columns = ['Cluster','No Cluster']
cm_df = pd.DataFrame(cm, columns, index)
plt.figure(figsize=(10, 6))
sns.heatmap(cm_df, annot=True)
plt.show()


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)
from sklearn.metrics import roc_curve, auc
n_classes = 2
# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
class_labels = ['Cluster','No Cluster']
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(Y_test[:, i], predictions[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

colors = ['blue', 'red']
for i, color, lbl in zip(range(n_classes), colors, class_labels):
    plt.plot(fpr[i], tpr[i], color = color, lw = 1.5,
    label = '{0} (auc = {1:0.3f})'.format(lbl, roc_auc[i]))
plt.plot([0, 1], [0, 1], 'k--', lw = 1.5)
plt.xlim([-0.05, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Opto-Net Roc Curve for Clustered Cells  ')
plt.legend(loc = 'lower right', prop = {'size': 11})
plt.show()