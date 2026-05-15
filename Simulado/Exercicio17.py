temp = float(input("Digite a temperatura atual (em graus Celsius):"))

if temp < 15:
    print("A temperatura está fria!")
elif 15 <= temp < 30:
    print("A temperatura está agradável!")
else:
    print("A temperatura está quente!")