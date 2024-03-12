# Exibindo uma mensagem do usuário

heroi = input("Qual o seu heroi favorito?\n")
print(heroi.title())

name = input("Digite o seu nome:\n")
print(name.title())

prompt = "Qual o seu nome?\n"
prompt += "E sobrenome?\n"

full_name = input(prompt)
print('Seu nome é: ' + full_name.title())
