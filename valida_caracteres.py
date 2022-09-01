nome = input("Digite seu nome:\n")
senha = input("Digite sua senha:\n")

if len(senha) < 10:
    print("senha invalida, a mesma deve ter mais que 10 caracters")
else:
    print('Olá, seu nome é ' + nome + ' e sua senha é ' + senha)
