# Dicionário é uma coleção de par chave-valor

dict = {
    'color': 'blue',
    'points': 10
}

print(dict)
print(dict['color'])

# Novos valores
dict['x'] = 0
dict['y'] = 1

print(dict)

# Removendo par chave-valor
del dict['y']
print(dict)

# Dicionario vazio
dict = {}

if dict:
    print('Dicionário com conteúdo.')
else:
    print('Esse dicionário está vazio.')
