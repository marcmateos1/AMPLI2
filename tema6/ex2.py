import numpy as np
def derivada(t,y):
    return y-t

h= 0.5
n= int(3/h)
t= np.linspace(0,3,n+1)
y= np.zeros(n+1)
y[0] = 1
for i in range (1,n+1):
    y[i] = y[i-1]+ (h/2)*derivada(t,y)+derivada( t+h, y[i-1]+h*derivada(t,y))