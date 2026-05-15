import numpy as np

matriz = np.random.randint(0, 100,(4, 4))

soma = np.trace(matriz)

print(f"Matriz:\n{matriz}")
print(f"A soma da diagonal principal é de : {soma}")