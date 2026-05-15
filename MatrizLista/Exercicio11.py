import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

lista = np.array([])

somas = matriz.sum(axis = 0).tolist()

print(f"Matriz:\n{matriz}")
print(f"Lista da soma das colunas: {somas}")