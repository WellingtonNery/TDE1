usuario_admin = "admin"
usuario_user = "usuario"
usuario_visit = "visitante"

senha_admin = "admin"
senha_usuario = "user"

usuario_tentativa = str(input("Digite o usuário que irá logar (admin, usuario ou visitante): "))

if usuario_tentativa == usuario_admin:
    admin_correta = str(input("Digite sua senha: "))
    if senha_admin == admin_correta:
        print("Login efetuado com sucesso!")
    else:
        print("Senha incorreta!")
elif usuario_tentativa == usuario_user:
    print("Digite sua senha:")
    usuario_correta = str(input("Digite sua senha: "))
    if senha_usuario == usuario_correta:
        print("Login efetuado com sucesso!")
    else:
        print("Senha incorreta!")
elif usuario_tentativa == usuario_visit:
    print("Inciando sessão de visitante!")