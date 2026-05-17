import conversor as cv
import texto as tx

altura = 5
temperatura = 17
frase = 'Olá, tenha um bom dia!'

print(f"Altura em centímetros: {cv.MetrosCm(altura)}cm")
print(f"Temperatura em Fahrenheit: {cv.CelsiusF(temperatura)}F")

print(f"Tamanho da frase: {tx.contador(frase)}")
print(f"Frase em maiúsculo: {tx.maiusculo(frase)}")