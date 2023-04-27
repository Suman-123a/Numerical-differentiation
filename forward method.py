#numerical differentiation
#forward method
import matplotlib.pyplot as plt
import numpy as np
def diff(xi,xf,n,f):
	h=(xf-xi)/(n-1)
	xx,yy,yy1=[],[],[]
	for i in range(n):
		x=xi+i*h
		xx.append(x)
		y=f(x)
		yy.append(y)
	for i in range(len(yy)-1):
		y1=(yy[i+1]-yy[i])/(xx[i+1]-xx[i])
		yy1.append(y1)
	return xx,yy1
def g(x):
	return np.sin(x)
z1,z2=diff(0,20,1000,g)
print(len(z2))
#z1[0:-1]...to exclude ta last value of x
plt.plot(z1[0:-1],z2,"--")
plt.show()
	
