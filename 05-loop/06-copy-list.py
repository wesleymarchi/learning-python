# Movendo herois para outra lista

unconfirmed_heros = ['batman', 'rorschach', 'america']
confirmed_heros = []

# Verifica e move os herois
while unconfirmed_heros:
    current_hero = unconfirmed_heros.pop()

    print('Verificando: ' + current_hero.title())
    confirmed_heros.append(current_hero)

# Exibe a nova lista de confirmados
print('\nThe following users have been confirmed: ')
for confirmed_hero in confirmed_heros:
    print(confirmed_hero.title())
