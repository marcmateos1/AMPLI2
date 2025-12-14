import math
#from scipy import stats

a=0
b=3
p=3/5
n=10
total=0

for i in range(a,b+1):
    print(i)
    probabilitat=math.comb(n,i)*(p**i)*((1-p)**(n-i))
    total=probabilitat+total

print(total)