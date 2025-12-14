import numpy as np
f= open("temps-posicio.txt", "r")
n=800
temps=np.array(n+1)
i=0
for line in f:
    trozos=line.strip().split()
    temps[i] = trozos[0]

print(temps)