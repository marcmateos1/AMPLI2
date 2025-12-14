#btcs
import numpy as np
t= np.linspace(0, 0.2, 4+1)
x= np.linspace(0,1, 4+1)
nt= len(t)
nx=nt
u=np.zeros((nx,nt))

#contorn
for i in range(nt):
    u[0, i]= 0
    u[-1, i] = 0
for k in range(nx):
    u[k,0]=np.sin(np.pi * x[k])

#mètode explicit FTCS
alpha = 1
dx= x[1]- x[0]
dt = t[1]-t[0]
landa = alpha**2 * dt/(dx**2)
print(landa) #>0.5

for j in range (nt-1):
    for i in range(1, nx-1):
        u[i,j+1] = (1-2*landa)*u[i,j] + landa*(u[i+1,j]+u[i-1,j])
        #altre manera que tmb serveix u[i,j+1]= u[i,j] + landa*(u[i-1,j]-2*u[i,j]+u[i+1,j])
print(u)

#mètode implicit simple, BTCS

# BTCS bàsic amb aproximació simple
for n in range(1, nt):
    for i in range(1, nx-1):
        u[i, n] = ((1 + 2*landa) * u[i, n-1] - landa * (u[i-1, n-1] + u[i+1, n-1]))
print(u)

#analitica
for i in range(nx):
    for i in range(nt):
        u[i,j]= np.exp(-(np.pi*t[j])*np.sin(np.pi*x[i]))
print(np.transpose(u))