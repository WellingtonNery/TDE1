def processar_dados(*args, **kwargs):
    for valor in args:
        print(valor)

    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")