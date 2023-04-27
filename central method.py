#numerical differentiation
#central method
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
	for i in range(1,len(yy)-1):
		y1=(yy[i+1]-yy[i-1])/(2*h)
		yy1.append(y1)
	return xx,yy1
def g(x):
	return np.exp(x)
z1,z2=diff(0,10,1000,g)
#z1[1:-1]...to exclude the first & last value of x
plt.plot(z1[1:-1],z2)
plt.show()
	
