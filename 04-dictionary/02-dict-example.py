# Dicionário com diversos valores

languages = {
    'batman': 'python',
    'superman': 'java',
    'rorschach': 'javascript',
    'escanor': 'python',
}

print("Batman's favorite language: " + languages['batman'].title())

# Loop em um dicionário
print("\nLoop em um dicionário: ")
for key, value in languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

# Loop nas chaves
print("\nLoop nas chaves: ")
for key in languages.keys():
    print(key.title())

# Loop ordenado com sorted()
print("\nLoop ordenado: ")
for hero in sorted(languages.keys()):
    print(hero.title())

# Loop dos valores
print("\nLoop dos valores")
for language in sorted(languages.values()):
    print(language.title())

# Conjunto, set() define um conjunto a partir de uma lista, com valores únicos
print("\nConjunto: ")
for language in set(languages.values()):
    print(language)
