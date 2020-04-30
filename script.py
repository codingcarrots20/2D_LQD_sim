from array import array
import numpy as np
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense  
import math
import matplotlib.pyplot as plt


N=100

No_of_files = 2000
name="data(100)"

D=[]
S=[]
Vx=[]
Vy=[]
Vx0=[]
Vy0=[]

def array_to_image(arr):
	img = np.empty([N,N],dtype="int")
	for i in range(0,N):
		for j in range(0,N):
			img[i][j]=math.floor(arr[j*N+i])
	
	plt.imshow(img)
	plt.show()
	print (img.shape)


for i in range(0,No_of_files+1):
	fname = name+"/D"+str(i)+".bin"
	f=open(fname,"rb")

	D0 = array('f')
	D0.fromfile(f,N*N)
	D.append(D0)



	f.close()

	fname = name+"/s"+str(i)+".bin"
	f=open(fname,"rb")

	s = array('f')
	s.fromfile(f,N*N)
	S.append(s)



	f.close()


	fname = name+"/Vx"+str(i)+".bin"
	f=open(fname,"rb")

	vx = array('f')
	vx.fromfile(f,N*N)
	Vx.append(vx)


	f.close()


	fname = name+"/Vy"+str(i)+".bin"
	f=open(fname,"rb")

	vy = array('f')
	vy.fromfile(f,N*N)
	Vy.append(vy)



	f.close()


	fname = name+"/Vx0"+str(i)+".bin"
	f=open(fname,"rb")

	vx0 = array('f')
	vx0.fromfile(f,N*N)
	Vx0.append(vx0)



	f.close()

	fname = name+"/Vy0"+str(i)+".bin"
	f=open(fname,"rb")

	vy0 = array('f')
	vy0.fromfile(f,N*N)
	Vy0.append(vy0)



	f.close()

Data_in=[]
for i in range(0,No_of_files+1):
	tmp=[]
	tmp.append(D[i])
	tmp.append(S[i])
	tmp.append(Vx[i])
	tmp.append(Vy[i])
	tmp.append(Vx0[i])
	tmp.append(Vy0[i])
	Data_in.append(tmp)

Data_out=[]
for i in  range(0,No_of_files):
	Data_out.append(Data_in[i+1])
	



Data_in.pop()

Data_in=np.array(Data_in)
Data_out=np.array(Data_out)

    
model =Sequential([
    Dense(N,input_shape=(6,N*N),activation="relu"),
	Dense(N*N,activation="relu"),

])
model.compile(loss="mean_squared_error",optimizer="sgd")
model.fit(Data_in,Data_out,epochs=100)

model.save("model.h5")
print("Saved model to disk")










