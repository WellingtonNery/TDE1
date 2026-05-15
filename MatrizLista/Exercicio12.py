import numpy as np

matriz = np.array([[12, 24, 36],
          [5, 10, 15],
          [3, 6, 9]])

matrizT = matriz.T

print(f"Matriz:\n{matriz}")

if np.array_equal(matriz, matrizT):
    print("A matriz é simétrica!")
else:
    print("A matriz não é simétrica!")