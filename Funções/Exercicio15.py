def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

mostrar_dados(nome = "Wellington", idade = 19, cidade = "Curitiba")
