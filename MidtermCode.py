import numpy as np
import pandas as pd
from PIL import Image
import glob
image_CNV_list = []
for filename in glob.glob('C:/Users/damia/Desktop/University of Cincinnati/2020 Spring Semester/Big Data/CNV/*.jpeg'):
    im = Image.open(filename)
    image_CNV_list.append(im)

image_NORMAL_list = []
for filename in glob.glob('C:/Users/damia/Desktop/University of Cincinnati/2020 Spring Semester/Big Data/NORMAL/*.jpeg'):
    im = Image.open(filename)
    image_NORMAL_list.append(im)
    
image_DME_list = []
for filename in glob.glob('C:/Users/damia/Desktop/University of Cincinnati/2020 Spring Semester/Big Data/DME/*.jpeg'):
    im = Image.open(filename)
    image_DME_list.append(im)
    
image_DRUSEN_list = []
for filename in glob.glob('C:/Users/damia/Desktop/University of Cincinnati/2020 Spring Semester/Big Data/DRUSEN/*.jpeg'):
    im = Image.open(filename)
    image_DRUSEN_list.append(im)
    

image_array = np.array([["Disease", "Image Average", "Image Std", "Image Median"]])


for index in image_CNV_list:
    matrix_average = np.average(index)
    matrix_std = np.std(index)
    matrix_median = np.median(index)
    temp_array = ([["CNV", matrix_average, matrix_std, matrix_median]])
    image_array = np.vstack([image_array, temp_array])  
    
for index in image_NORMAL_list:
    matrix_average = np.average(index)
    matrix_std = np.std(index)
    matrix_median = np.median(index)
    temp_array = ([["NORMAL", matrix_average, matrix_std, matrix_median]])
    image_array = np.vstack([image_array, temp_array])  
    
for index in image_DME_list:
    matrix_average = np.average(index)
    matrix_std = np.std(index)
    matrix_median = np.median(index)
    temp_array = ([["DME", matrix_average, matrix_std, matrix_median]])
    image_array = np.vstack([image_array, temp_array])  
    
for index in image_DRUSEN_list:
    matrix_average = np.average(index)
    matrix_std = np.std(index)
    matrix_median = np.median(index)
    temp_array = ([["DRUSEN", matrix_average, matrix_std, matrix_median]])
    image_array = np.vstack([image_array, temp_array])  
    
df = pd.DataFrame(image_array)
path = "C:/Users/damia/Desktop/University of Cincinnati/2020 Spring Semester/Big Data/ImageMatrixOutput.csv"
df.to_csv(path, index=False, header = False)
