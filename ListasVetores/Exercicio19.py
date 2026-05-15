numeros = [7, -12, 3, 18, -5, 0, 14, -9, 2, -1, 11, -7, 6, -3, 20, -15, 4, 9, -2, 13]

max_atual = numeros[0]
max_global = numeros[0]

for i in range(1, len(numeros)):
    max_atual = max(numeros[i], max_atual + numeros[i])
    max_global = max(max_global, max_atual)

print("Maior soma contígua:", max_global)