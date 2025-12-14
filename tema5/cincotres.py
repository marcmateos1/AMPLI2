import numpy as np
import matplotlib.pyplot as plt
f= open("t0-h-pos.txt", "r")
i=0
pos=[]

for line in f:
    if i ==0:
        t0= float(line)
    elif i==1:
        h= float(line)
    else:
        pos.append(float(line))
    i+=1
f.close()

pos = np.array(pos)
t= t0 + np.arange(len(pos))*h

print(t)
plt.plot(t,pos)
plt.show()


#b) dibuixar v(t)
v=np.zeros(len(pos))
for i in range(len(pos)-1):
    y1= pos[i+1]
    y2=pos[i]
    v[i]=((y1-y2)/h)
plt.plot(t, v)
plt.show()
