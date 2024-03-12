# Passando um número arbitrario de argumentos
def heros(size, *list_heros):
    """ Exibe uma lista de herois. """

    print("\nTamanho: " + str(size))
    for hero in list_heros:
        print(hero)


heros(6, 'batman')
heros(9, 'rorschach', 'joker', 'homelander')
