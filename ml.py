from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.models import Sequential
from keras.layers import Dense


import matplotlib.pyplot as plt
import numpy as np

N = 16

array_of_3_pixels=[]
iteration=[]
tmp=[]
for i in range(1,31):
    imgD=(img_to_array(load_img("./Experiment0/renderD/screen-"+str(i).zfill(4)+".tif")))
    imgV=(img_to_array(load_img("./Experiment0/renderV/screen-"+str(i).zfill(4)+".tif")))
    imgV0=(img_to_array(load_img("./Experiment0/renderV0/screen-"+str(i).zfill(4)+".tif")))

    for j in range(0,N):
        for k in range(0,N):
            tmp.append( imgD  [j][k])
            tmp.append( imgV  [j][k])
            tmp.append( imgV0 [j][k])
            array_of_3_pixels.append( tmp )
            tmp=[]
    
    iteration.append(array_of_3_pixels)
    array_of_3_pixels=[]

            



train_y_array = []
for i in range(1,30):
    train_y_array.append(iteration[i])

iteration.pop()

train_x=np.array(iteration)
train_y=np.array(train_y_array)

    

print(train_x.shape)
print(train_y.shape)




















