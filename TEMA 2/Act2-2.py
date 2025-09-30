import math
#from scipy import stats

a=5
b=5
p=5/8
n=8
total=0

for i in range(a,b+1):
    print(i)
    probabilitat=math.comb(n,i)*(p**i)*((1-p)**(n-i))
    total=probabilitat+total

print(probabilitat)