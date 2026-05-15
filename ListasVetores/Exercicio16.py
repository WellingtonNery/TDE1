lista1 = [1, 5, 8, 10, 16]
lista2 = [2, 3, 4, 5 , 7, 10, 13, 16]
interseccao = []

for i in lista1:
    if i in lista2:
        interseccao.append(i)

print(interseccao)