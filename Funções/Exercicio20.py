def executar(funcao, *valor):
    return funcao(*valor)

def somar(a, b):
    return a + b

print(executar(somar, 10, 15))