import numpy as np
import matplotlib.pyplot as plt
t0=0
tf=2
y0=1
h=0.1
n= int((tf-t0)/h)
t=np.linspace(t0, tf, n+1)

def derivada(t,y):
    return t+y
def euler(tA,tB,yA,h):
    y=np.zeros(n+1)
    y[0] = yA
    for i in range(n-1):
        y[i+1] = y[i]+ h * derivada(t[i], y[i])
    return y
resultat = euler(t0, tf, y0, h)
plt.plot(t, resultat)
plt.show()