n = int(input("Tamanho da matriz n x n: "))

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

rotacionada = []

for i in range(n):
    rotacionada.append([0] * n)

for i in range(n):
    for j in range(n):
        rotacionada[j][n - 1 - i] = matriz[i][j]

print("\nMatriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz rotacionada:")
for linha in rotacionada:
    print(linha)