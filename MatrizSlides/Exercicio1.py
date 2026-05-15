import numpy as np

manha = np.array([[27, 32, 38],
                  [0, 2, 5],
                  [17, 13, 18]])

tarde = np.array([[0, 2, 3],
                  [4, 4, 6],
                  [30, 19, 23]])

total = manha + tarde

print(f"Matriz manhã:\n{manha}")
print(f"Matriz tarde:\n{tarde}")
print(f"Matriz total:\n{total}")