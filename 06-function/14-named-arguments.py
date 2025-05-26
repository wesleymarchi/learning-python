# Passando um número arbitrario de argumentos nomeados, ** representa um dicionario

def profile(first, last, **users):
    """ Construindo um dicionário de nomes. """

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in users.items():
        profile[key] = value

    return profile


first_name = input('Digite o nome: ')
last_name = input('Digite o sobrenome: ')

user = profile(first_name, last_name,
               location='israel',
               tech='mark i',
               controle='manual')

print(user)
