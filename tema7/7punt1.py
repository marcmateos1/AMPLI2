import numpy as np
delta= 1/3
x= np.linspace(1,2, int((2-1)/delta)+1)
y=np.linspace(0,1, int(1/delta)+1)

u= np.zeros((len(x), len(y)))
#calcul parametres
alpha = 1
dx = x[1]-x[0]
dy = y[1]-y[0]
landa= alpha**2* dx/(dy**2)
print(landa)
#contorns
for i in range(len(x)):
    u[i,0]= 2*np.log(x[i])
    u[i,-1] = np.log(x[i]**2 +1)

for j in range(len(y)):
    u[0, j]=np.log(y[j]**2 +1)
    u[-1,j]=np.log(y[j]**2 +4)

for i in range(1, len(x)-1):
    for j in range(1, len(y)-1):
        #u[i, j] =  (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])/4
        u[i,j]= (1+2*landa)*u[i,j-1]-landa*(u[i-1,j-1]+u[i+1,j-1])
        
print(np.transpose(u))