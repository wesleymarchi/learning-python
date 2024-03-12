# Deletando um item

heros = ['iron man', 'batman', 'doctor stranger', 'rorschach']
print(heros)

del heros[-1]
print(heros)

# Remove o ultimo item de uma lista
remove_hero = heros.pop()
print(heros)
print("Item removido: " + remove_hero)

# Removendo a partir do indice
remove_first_hero = heros.pop(0)
print(heros)

# Removendo pelo valor - apenas a primeira ocorrencia
heros.remove('batman')
print(heros) # Lista vazia
