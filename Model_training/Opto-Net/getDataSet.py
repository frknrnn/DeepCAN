import pandas as pd
import numpy as np
import os

class dataSet():
    def getData(self,live_cell_path,dead_cell_path):
        live_cell_folder_path = live_cell_path
        dead_cell_folder_path = dead_cell_path

        ############## READ LİVE CELL ##############
        live_cell = []
        live_cell_folder = os.listdir(live_cell_folder_path)
        for i in live_cell_folder:
            temp_list = pd.read_csv(live_cell_folder_path + "/" + str(i), sep=',', engine='python')
            temp_list = temp_list.values.tolist()
            live_cell = live_cell + temp_list


        ############## READ DEAD CELL ##############
        dead_cell = []
        dead_cell_folder = os.listdir(dead_cell_folder_path)
        for i in dead_cell_folder:
            temp_list = pd.read_csv(dead_cell_folder_path + "/" + str(i), sep=',', engine='python')
            temp_list = temp_list.values.tolist()
            dead_cell = dead_cell + temp_list

        print("Live Cell Size:" + str(len(live_cell)))
        print("Dead Cell Size:" + str(len(dead_cell)))

        new_dead_cell = []
        for i in dead_cell:
            new_dead_cell.append(i)
            i = np.array(i).reshape(50, 50)
            new_dead_cell.append(np.flip(i, 0).reshape(2500))
            new_dead_cell.append(np.flip(i, 1).reshape(2500))


        print("New Dead Cell Size:" + str(len(new_dead_cell)))

        ############## MERGE CELLS DATA ###########
        X = live_cell + new_dead_cell

        ############### CREATE LABEL ##############
        # Live = 1
        # Dead = 0
        Y = []
        for i in range(len(live_cell)):
            Y.append(1)
        for i in range(len(new_dead_cell)):
            Y.append(0)

        return X,Y