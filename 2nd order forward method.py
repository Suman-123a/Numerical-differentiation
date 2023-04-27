#2nd order derivative by Forward method
import matplotlib.pyplot as plt
import numpy as np
def diff(xi,xf,n,f):
	h=(xf-xi)/(n-1)
	xx,yy,yy1,yy2=[],[],[],[]
	for i in range(n):
		x=xi+i*h
		xx.append(x)
		y=f(x)
		yy.append(y)
	for i in range(len(yy)-1):
		y1=(yy[i+1]-yy[i])/(xx[i+1]-xx[i])
		yy1.append(y1)
		#yy1=999
	for i in range(len(yy1)-1):
		y2=(yy1[i+1]-yy1[i])/(xx[i+1]-xx[i])
		yy2.append(y2)
		
	return xx,yy2
def g(x):
	return np.exp(x)
g1,g2=diff(0,10,1000,g)
plt.plot(g1[0:-2],g2)
plt.show()

	
