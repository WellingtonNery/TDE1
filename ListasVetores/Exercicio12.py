inteiros = [1,2,3,4,5,6,7,8,9,10]
maior = 1
menor = 1

for i in inteiros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")