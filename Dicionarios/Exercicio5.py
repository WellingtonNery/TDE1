dicionario = {"Nome": "Melissa", "Idade": 19, "Cidade":"Curitiba"}
print(dicionario)
escolha = input("Deseja limpar o dicionario? ")
if escolha=="Sim" or escolha=="sim":
    dicionario.clear()
    print(dicionario)
else:
    print(dicionario)