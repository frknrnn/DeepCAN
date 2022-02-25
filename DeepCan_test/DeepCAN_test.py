from AI_count import AI_count
import cv2

##### MAİN CODE #####

unet_path = "C:/Users/optof/PycharmProjects/DeepCan/DeepCan_test/Model_weights/a2780_vgg16_unet_w0.hdf5"
cnn_path = "C:/Users/optof/PycharmProjects/DeepCan/DeepCan_test/Model_weights/v3_viability.h5"
cluster_path= "C:/Users/optof/PycharmProjects/DeepCan/DeepCan_test/Model_weights/v1_cluster.h5"


test_image_path = "C:/Users/optof/PycharmProjects/CellAnalyzer/DeepCAN_DataSets/CountingTestDataSet/A549/a549-1.jpeg"
result_path = "result.tif"
unet_output = "unet_result.tif"


#Standard
device_calibration = 0.650

size = 50
threshold = 242  ###0-255     /// 55 = 140 65=165 75=191 85=217 95=242
viability_flag = True

##### Read Test Image #####
test_image = cv2.imread(test_image_path)

##### SET PARAMETERS #####
AI = AI_count()
AI.setParameters(device_calibration,size)
AI.setModelPath_hdf5(unet=unet_path,cnn=cnn_path,output=unet_output,threshold=threshold,cluster_cnn=cluster_path)

split1 = AI.crop_image(test_image,128,0,0)
split2 = AI.crop_image(test_image,128,20,20)

unet1 = AI.AI_threshold(split1)
unet2 = AI.AI_threshold(split2)

#new_merge1 = AI.ind_corner(unet1)

merge1 = AI.merge_image2(unet1,128,128,3264,2448,0,0)
merge2 = AI.merge_image2(unet2,128,128,3264,2448,20,20)
merge3 = merge1|merge2
merge3 = cv2.GaussianBlur(merge3,(3,3),0)
ret3, merge3 = cv2.threshold(merge3, 150, 255, cv2.THRESH_BINARY)

copy_image=test_image.copy()

##### FindCells and Viability #####
result_image = AI.findCells(merge3, copy_image,viability_flag)

totalCellDiameter,totalCellContour,liveCellDiameter, liveCellContour, deadCellDiameter, deadCellContour = AI.getParameters()
print("Total")
print(len(totalCellDiameter))
print("Live")
print(len(liveCellDiameter))
print("Dead")
print(len(deadCellDiameter))

################### Save Result ######################
cv2.imwrite(result_path,result_image)
