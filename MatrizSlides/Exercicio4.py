import numpy as np

salarios = np.array([[1612, 1021, 1930],
                     [5213, 6150, 5789],
                     [7000, 9562, 13213]])

salariosDps = salarios * 1.1

print(f"Salários atualizados:\n{salariosDps}")