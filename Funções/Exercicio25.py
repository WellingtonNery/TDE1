def contagem(n):
    if n < 0:
        print("Fim!")
        return
    print(n)
    contagem(n - 1)

contagem(10)