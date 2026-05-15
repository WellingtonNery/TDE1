import numpy as np

matriz = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o numero [{i+1},{j+1}]: "))

num = float(input("Digite um número real: "))

matrizMult = matriz * num

print(matrizMult)