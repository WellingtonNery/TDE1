numeros = [1, 6, 8, 8, 10, 6, 2, 1, 3]
semRep = []

for i in numeros:
    if i not in semRep:
        semRep.append(i)

print(semRep)