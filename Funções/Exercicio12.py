def saudacao(nome, periodo='dia'):
    if periodo == 'dia':
     print(f"Bom {periodo}, {nome}!")
    else:
        print(f"Boa {periodo}, {nome}!")

saudacao('Wellington', 'noite')