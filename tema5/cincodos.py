#importar fitxer
import matplotlib.pyplot as plt
import numpy as np

f= open("temps-posicio.txt", "r")
#(a) Llegeix les mesures i dibuixa la gr`afica de la funci´o posici´o.

temps=[]
posicions=[]

for line in f:
    trozos= line.strip().split()
    temps.append(float(trozos[0]))
    posicions.append(float(trozos[1]))
f.close()


plt.plot(temps,posicions)
plt.show()

#(b) Utilitza les aproximacions de la derivada i de la derivada segona:
temps=np.array(temps)
posicions=np.array(posicions)

#pas entre cada interval de temps
h= temps[1]-temps[0]
n=len(temps)
#endavant
y=np.exp(temps) #y= funció
y2=np.exp(temps+h) 
y3=np.exp(temps-h)
d= np.zeros(n+1) #llista vel derivada
d2= np.zeros(n+1) #llista acc derivada segona

for i in range(n+1): #omplir llistes de derivades
    d[i] = (y2[i]-y[i])/h
    d2[i] = (y3[i]-2*y[i]+y3[i])/h**2


plt.plot(temps, d)
plt.show()
plt.plot(temps,d2)
plt.show()

#c) calcular derivada (dmodificada) en l'instant t=400
dmodificada= (-np.exp(temps+2*h)+8*y2-8*y3+np.exp(temps-2*h))/12*h
print("La velocitat en l'instant 400 és", dmodificada[4], "m/s")

# Si el temps est`a mesurat en milisegons i la posici´o en cent´ımetres, calcula les velocitats
#mitjanes en Km/h en la primera meitat de l’interval i en la segona meitat de l’interval.

vmitj1 = np.zeros[n/2 +1] 
temps= temps*(10**3)*3600 #en h
posicions = posicions*100*1000 #en km
for i in range (n/2):
    vmitj1.append(d[i])
    