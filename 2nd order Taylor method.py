#second order derivative(taylor method)
import matplotlib.pyplot as plt
import numpy as np
def sdiff(xi,xf,n,f):
	h=(xf-xi)/(n-1)
	xx,yy,yy1=[],[],[]
	for i in range(n):
		x=xi+i*h
		xx.append(x)
		y=f(x)
		yy.append(y)
	for i in range(1,len(yy)-1):
		y1=(yy[i+1]+yy[i-1]-2*yy[i])/(h**2)
		yy1.append(y1)
	return xx,yy1
def g(x):
	return (1/6)*x**3
z1,z2=sdiff(0,20,1000,g)
plt.plot(z1[1:-1],z2)
plt.show()
	