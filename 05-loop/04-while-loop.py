# Laço de repetição while

x = 1

# Contando de 1 até 5
while x <= 5:
    print(x)
    x += 1

# Podemos definir uma flag para que o usuário decida quando sair do laço
while x != 0:
    print(x)
    x = input("Insira o valor de x - 0 para sair\n")
    x = int(x)

prompt = "Escreva o nome de um heroi ou 'sair' para finalizar\n"
heroi = ""

while heroi != 'sair':
    heroi = input(prompt)
    print(heroi)

# Flag conforme uma condição
active = True
while active:
    name = input("Insira seu nome: \n")

    if name == 'sair':
        active = False
    else:
        print(name)
