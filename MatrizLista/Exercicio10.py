import numpy as np

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

matriz = np.zeros((linhas, colunas))

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input(f"Digite um valor {i+1},{j+1}: "))

print(f"Matriz:\n{matriz.T}")
