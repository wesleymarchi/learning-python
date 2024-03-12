# Verificando se um item consta em uma lista

heros = ['batman', 'superman', 'spiderman', 'rorschach']

print('aquaman' in heros)

# Verificando se um item não consta em uma lista
hero = 'aquaman'

if hero not in heros:
    print(hero.title() + " " + "não consta na lista")
