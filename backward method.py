#backward numerical differentiation

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
	for i in range(1,len(yy)):
		y1=(yy[i]-yy[i-1])/(xx[i]-xx[i-1])
		yy1.append(y1)
	return xx,yy1
def g(x):
	return 0.5*x**2
z1,z2=diff(0,20,1000,g)
#z1[0:-1]...to exclude ta last value of x
plt.plot(z1[0:-1],z2,"--")
plt.show()
	
