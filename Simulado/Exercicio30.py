contador = 0

for i in range (0, 5):
    nota = float(input(f"Digite a {i+1} nota: "))
    if nota >= 7:
        contador += 1

print(f"Quantidade de notas maiores ou iguais a 7: {contador}")