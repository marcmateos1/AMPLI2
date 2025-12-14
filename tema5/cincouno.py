import numpy as np

#np.linspace()
#y= np.e**x --> si x es un vector m'eleva tot de la llista
def endavant(f, x, h):
    return(f(x+h)-f(x))/(h)
f=np.exp
#DISCRETITZAR L'INTERVAL
x=np.linspace(1, 2, 101)#x es una llista de 101 nombres entre l'1 i el 2 [o bé np.arrange(1,2,0.01) (pero arriba fins el 1.99)]

h= 0.0001

approx = endavant(f, x, h)

print("aprox f'(x)=", approx)
