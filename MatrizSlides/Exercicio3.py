import numpy as np

ingredientes = np.array([[1, 3],
                         [3, 5],
                         [5, 2]])

pedidos =  np.array([[10],
                     [12],
                     [5]])

mtResultado = ingredientes * pedidos

print(f"Resultado:\n{mtResultado}")