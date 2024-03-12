# Inserindo dados de usuário

responses = {}

# Flag de enquete ativa
active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("Country? ")

    # Armazena a resposta no dicionário
    responses[name] = response

    # Verifica a continuação da enquete
    repeat = input("Another response? ")
    if repeat == 'no':
        active = False

# Exibe o resultado
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " from " + response + ".")
