def Factorial(a):
    if a == 0 or a==1:
        a=1
        return a

    resultado=1
    for i in range(a):
        resultado=resultado*(i+1)
    return resultado

def Perm(n,k):
    return((Factorial(n))/(Factorial(n-k)))
def PermR(n,k):
    return (n**k)
def Comb(n,k):
    return((Perm(n,k))/(Factorial(k)))
def CombR (n,k):
    return Comb(n+k-1,n-1)