# Modificando lista em função


def print_heros(unprinted_heros, completed_heros):
    """ Imprime herois e transfere para outra lista """

    while unprinted_heros:
        current_hero = unprinted_heros.pop()

        print("Printing hero: " + current_hero.title())
        completed_heros.append(current_hero)


def show_completed(completed_heros):
    """ Exibe os herois """
    print("\nHerois: ")
    for completed_hero in completed_heros:
        print(completed_hero.title())


unprinted_heros = ['iron man', 'batman', 'rorschach']
completed_heros = []

# Passa a lista como cópia
print_heros(unprinted_heros[:], completed_heros)
print("\n****** + ****** + *******")
show_completed(completed_heros)
