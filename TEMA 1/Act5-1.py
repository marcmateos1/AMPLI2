from Formules import*
#Per calcular els nombres diferents s'han de tenir en compte el nombre de xifres significatives
xifres= 11
total=0
for i in range(xifres):
    combinacions=9*Perm(9,i-1)
    total=total+combinacions

print("Hi ha una quantitat de", int(total), "possibilitats")