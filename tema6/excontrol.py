import matplotlib.pyplot as plt
import numpy as np
t0= 0
y0= 1
tf = np.pi/2
def derivada(t,y):
    return t*y+np.cos(y)
harray = [1/2, 1/4]
for h in harray:
    n=int((tf-t0)/h)
    te = np.linspace(t0,tf,n)
    ye = np.zeros(n)
    ye[0]=y0
    for i in range(1,n-1):
        ye[i+1] = ye[i]+h*derivada(te[i], ye[i])

plt.plot(te,ye)
plt.legend()
plt.show()