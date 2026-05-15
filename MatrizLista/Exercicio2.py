import numpy as np

tamanho = int(input("Digite o tamanho da matriz identidade: "))

identidade = np.eye(tamanho)

print(f"Matriz identidade:\n{identidade}")
