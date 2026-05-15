import numpy as np

estoque_inicial = np.array([[50, 16, 79],
                           [10, 2, 36],
                           [17, 56, 89]])

vendidos = np.array([[10, 2, 36],
                     [0, 1, 7],
                     [7, 26, 60]])

estoque_final = estoque_inicial - vendidos

print(f"Estoque inicial:\n{estoque_inicial}")
print(f"Vendidos:\n{vendidos}")
print(f"Estoque final:\n{estoque_final}")