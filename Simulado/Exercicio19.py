preco = float(input("Digite o valor da compra:"))

if 100 < preco <= 200:
    preco = preco * 0.9
elif preco > 200:
    preco = preco * 0.8

print(f"O preço final é de: {preco:.2f}")