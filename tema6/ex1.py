import numpy as np
import matplotlib.pyplot as plt

def derivada(t,y):
    return (t**2)/(y-1)

h=0.25
n= int((2-1)/h) #numero de passos
t=np.linspace(1,2,n+1) #n+1 pq falta el punt del subzero
y=np.zeros(n+1)
y[0]=3 #imatge de t subzero

for i in range(1,n+1):
    y[i] = y[i-1] + derivada(t[i-1]+h,y[i-1])*h
print(y[2])

#b

#c
lh = [0.25, (1/8),(1/16)] #assignar valors a h
lt = []
ly= []

for h in lh:
    n= int((2-1)/h)
    t=np.linspace(1,2,n+1)
    lt.append(t) 
    y=np.zeros(n+1)
    y[0]=3
    for i in range(1,n+1):
        y[i]=y[i-1] + derivada(t[i-1]+h,y[i-1])*h
    ly.append(y)

for k in range(3): #plotejar les aproximacions de les h
    plt.plot (lt[k], ly[k])
    

t= np.linspace(1,2)
real=1+ np.sqrt((2/3)*((t**3)+5))

plt.plot(t,real) #plotejar la real
plt.show()