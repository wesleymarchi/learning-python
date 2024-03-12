# Fatiando uma lista

heros = ['batman', 'superman', 'spiderman', 'rorschach', 'joker']

print(heros[0:3]) # três primeiros
print(heros[:3]) # três primeiros
print(heros[1:4]) # segundo até o terceiro
print(heros[2:]) # terceiro até o final
print(heros[-2:]) # exibe dois itens a partir do fim da lista

# Loop com fatias
for hero in heros[:3]:
    print(hero)
