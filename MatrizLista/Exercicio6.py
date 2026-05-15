import numpy as np

matriz = np.random.randint(1, 100, (3, 4))
pares = 0

print(f"Matriz:\n{matriz}")

for i in range(3):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares += 1

print(f"A matriz possui {pares} números pares!")

