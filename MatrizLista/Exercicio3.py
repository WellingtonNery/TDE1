import numpy as np

matriz = np.array([[20, 16, 3],
                   [30, 19, 16],
                   [48, 12, 5]])

busca = int(input("Digite o numero que deseja buscar na matriz: "))

boole = False
for i in matriz:
    for j in i:
        if busca == j:
            boole = True

if boole:
    print("O número foi encontrado na matriz!")
else:
    print("O número não foi encontrado na matriz!")

print(f"Matriz:\n{matriz}")
