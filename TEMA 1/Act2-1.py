from Formules import*

n=int(input("Digues el valor de n: "))
k=int(input("Digues el valor de k: "))

a=PermR(n,k)
b=CombR(n,k)

print("La Permutació amb repetició val:", a)
print("La Combinació amb repetició val", b)