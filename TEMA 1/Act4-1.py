from Formules import*

n=int(input("Valor de n pel triangle de Pascal: "))

fila=[]
n=n+1
for i in range(n):
    a=i+1
    for b in range(a):
        fila.append(Comb(i,b))
    print(fila)
    fila=[]0