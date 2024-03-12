# Lista

heros = ['batman', 'superman', 'spiderman', 'rorschach']

favorite_heros = ['batman', 'rorschach', 'aquaman']

for favorite_hero in favorite_heros:
    if favorite_hero in heros:
        print(favorite_hero.title() + ' esta na lista de favoritos')
    else:
        print('\n' + favorite_hero.title() + ' não consta na lista original.')
