contador = 0

for i in range (0, 10):
    num = float(input(f"Digite o {i+1} número: "))
    if num > 5:
        contador += 1

print (f"Foram digitados {contador} números maiores que 5!")