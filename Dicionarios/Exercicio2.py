produtos = {"boneca": "15,99", "novelo de lã": "20,99", "relogio": "59,99"}

alteracao = input("Digite o produto que deseja mudar o preço (boneca, novelo de lã ou relogio):")
preco = float(input(f"Digite o novo preço para o produto {alteracao}:"))

produtos[alteracao] = preco

print(f"Novo preço do produto {alteracao}: R${produtos[alteracao]}")

