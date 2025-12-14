import numpy as np
import matplotlib.pyplot as plt
h=[0.25, (1/8), (1/16)]
lt= []
ly=[]
def yprima(t,y):
    return ((y**2)+y)/t
for h in h:
    n=int((3-1)/h)
    t=np.linspace(1,3,n+1)
    lt.append(t)
    y=np.zeros(n+1)
    y[0]=-2
    for i in range(1,n+1):
        y[i]= y[i-1]+h*yprima(t[i-1],y[i-1])
    ly.append(y)
for k in range(3):
    plt.plot(lt[k], ly[k])

#plot analitica
def yreal(t):
  return (2*t)/(1-(2*t))
t_analitica = np.linspace(1, 3, 1000)  # vector temps suau
y_analitica = yreal(t_analitica)
plt.plot(t_analitica, y_analitica)
plt.show()

#b.1) calcular euler
for i in range(n+1):
    h=1/8
    y[i] = y[i-1] + h*yprima(y[i-1], t[i-1]) 
    if (t[i]==3):
        print(y[i])
        break
#b.2) calcular rungekutta punt mig
for i in range(n+1):
    h= 1/8
    y[i]= y[i-1] + h * (yprima(t[i-1]+(h/2), y[i-1]+ (h/2))* yprima(t[i-1], y[i-1]))
    if abs(y[i]) > 1e6:   # si creix massa
        print("Overflow a i =", i)
        break
    if (t[i]==3):
        print(y[i])
        break