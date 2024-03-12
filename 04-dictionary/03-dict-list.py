# Definindo uma lista de dicionários

batman = {
    'color': 'black',
    'social': 'not',
}

superman = {
    'color': 'blue',
    'social': 'yes',
}

heros = [batman, superman]

for hero in heros:
    print(hero)

# Define soldados
soldiers = []
for soldier in range(10):
    new_soldier = {'velocidade': 10, 'forca': 6, 'inteligencia': 5}
    soldiers.append(new_soldier)

# Exibe os soldados - 5 primeiros
for soldier in soldiers[:5]:
    print(soldier)

print("Quantidade de soldados: " + str(len(soldiers)))
