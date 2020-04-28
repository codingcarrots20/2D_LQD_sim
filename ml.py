
from matplotlib import image
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense  

import numpy as np
N = 16




def convToImageAndShow (data):
    # data is N*N , 3 ,3
    img_D = np.empty((0,N,3),int)
    img_V = np.empty((0,N,3),int)
    img_V0 = np.empty((0,N,3),int)
    
    img_D_pix=np.empty((0,3),int)
    img_V_pix=np.empty((0,3),int)
    img_V0_pix=np.empty((0,3),int)
    
    for i in range(0,(N)):
        for j in range (0,(N)):
            img_D_pix = np.append(img_D_pix , [data[ i*N + j ][0]], axis=0)
            img_V_pix = np.append(img_V_pix , [data[ i*N + j ][1]], axis=0)
            img_V0_pix = np.append(img_V0_pix , [data[ i*N + j ][2]], axis=0)
            
        img_D= np.append(img_D ,np.expand_dims(img_D_pix,axis=0), axis=0)
        img_V= np.append(img_V ,np.expand_dims(img_V_pix,axis=0), axis=0)
        img_V0= np.append(img_V0 ,np.expand_dims(img_V0_pix,axis=0), axis=0)
        
        img_D_pix=np.empty((0,3),int)
        img_V_pix=np.empty((0,3),int)
        img_V0_pix=np.empty((0,3),int)

    fig = pyplot.figure()
    ax1= fig.add_subplot(1,3,1)
    ax1.imshow(img_D)
    ax2= fig.add_subplot(1,3,2)
    ax2.imshow(img_V)
    ax3= fig.add_subplot(1,3,3)
    ax3.imshow(img_V0)
    pyplot.show()
            


array_of_3_pixels=[]
iteration=[]
tmp=[]
for i in range(1,31):
    imgD=(image.imread("./Experiment0/renderD/screen-"+str(i).zfill(4)+".tif"))
    imgV=(image.imread("./Experiment0/renderV/screen-"+str(i).zfill(4)+".tif"))
    imgV0=(image.imread("./Experiment0/renderV0/screen-"+str(i).zfill(4)+".tif"))

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

    

mode = Sequential([
    Dense(N*N, input_shape=(N*N,3,3))
])

print(model.predict([train_x[1]]))






















