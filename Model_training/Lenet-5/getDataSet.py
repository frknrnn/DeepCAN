import pandas as pd
import numpy as np
import os

class dataSet():
    def getData(self, cluster_path, single_cell_path):
        cluster_folder_path = cluster_path
        single_cell_folder_path = single_cell_path

        ############## READ CLUSTER CELLS ##############
        cluster = []
        cluster_folder = os.listdir(cluster_folder_path)
        for i in cluster_folder:
            temp_list = pd.read_csv(cluster_folder_path + "/" + str(i), sep=',', engine='python')
            temp_list = temp_list.values.tolist()
            cluster = cluster + temp_list



        ############## READ NO CLUSTER CELLS ##############
        single_cells = []
        no_cluster_folder = os.listdir(single_cell_folder_path)
        for i in no_cluster_folder:
            temp_list = pd.read_csv(single_cell_folder_path + "/" + str(i), sep=',', engine='python')
            temp_list = temp_list.values.tolist()
            single_cells = single_cells + temp_list

        print("Cluster:" + str(len(cluster)))
        print("Single Cells:" + str(len(single_cells)))

        single_cells = single_cells[0:1500]


        augmented_cluster_cells = []
        for i in cluster:
            augmented_cluster_cells.append(i)
            i = np.array(i).reshape(50, 50)
            augmented_cluster_cells.append(np.flip(i, 0).reshape(2500))
            augmented_cluster_cells.append(np.flip(i, 1).reshape(2500))



        print("Augmented Cluster Size:" + str(len(augmented_cluster_cells)))

        ############## MERGE CELLS DATA ###########
        X = single_cells+augmented_cluster_cells

        ############### CREATE LABEL ##############
        # SingleCells = 1
        # Cluster = 0

        Y = []
        for i in range(len(single_cells)):
            Y.append(1)
        for i in range(len(augmented_cluster_cells)):
            Y.append(0)

        return X,Y