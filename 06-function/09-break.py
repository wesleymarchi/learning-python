# Flag de saída
def get_hero(first_name, last_name):
    """ Retorna nome e sobrenome """

    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("(q quit)")

    first_name = input("First name: ")
    if first_name == 'q':
        break

    last_name = input("Last name: ")
    if last_name == 'q':
        break

    name = get_hero(first_name, last_name)
    print("\nHello, " + name)
