import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
#matplotlib inline

def f(x):
    if (np.abs(x)<1e-10):
        res = x
    else:
        #res = x*np.sin(1.0/x)
        res = np.sin(x)/x
    return res

X = np.arange(-10,10,0.01)

#plot(X,f(X))

def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        y,err = integrate.quad(f,0,val)
        res[i]=y
    return res

T = 10


#plt.plot(X,2*(F((np.pi*(X+T))/T)-F((np.pi*(X-T))/T)))
#plt.plot(X,(1.0/2.0)*2*(F((2*np.pi*(X+T))/T)-F((2*np.pi*(X-T))/T)))
#plt.plot(X,(1.0/3.0)*2*(F((3*np.pi*(X+T))/T)-F((3*np.pi*(X-T))/T)))
#plt.plot(X,(1.0/4.0)*2*(F((4*np.pi*(X+T))/T)-F((4*np.pi*(X-T))/T)))
#plt.plot(X,(1.0/5.0)*2*(F((5*np.pi*(X+T))/T)-F((5*np.pi*(X-T))/T)))
#plt.plot(X,(1.0/6.0)*2*(F((6*np.pi*(X+T))/T)-F((6*np.pi*(X-T))/T)))
n=100
#plt.plot(X,(1.0/(2*np.pi))*2*(F((n*np.pi*(X+T))/T)-F((n*np.pi*(X-T))/T)))
plt.plot(X,(1.0/(np.pi))*(F(n*(np.pi-((np.pi*X)/T)))+F(n*(np.pi+((np.pi*X)/T)))))
#plt.plot(X,2*(F((n*4*pow(np.pi,2)*(X+T))/T)-F((n*4*pow(np.pi,2)*(X-T))/T)))
plt.show()