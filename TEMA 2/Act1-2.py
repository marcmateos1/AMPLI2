import matplotlib.pyplot as plt
import math
#math.comb(a,b)

#n=10
#x=range(n)
#print(x)
#y=range(1,2*n,2)
#plt.bar(x,y)
#plt.show()

n=1000
x=range(n+1)
p=0.4
y=[]

for k in x:
    y.append(math.comb(n,k)*(p**k)*((1-p)**(n-k)))

plt.bar(x,y)
plt.show()



