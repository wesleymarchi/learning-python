# Lista dentro de um dicionário

soldier = {
    'country': 'brasil',
    'vacations': ['argentina', 'chile', 'canada'],
}

print("Nacionalidade: " + soldier['country'].title())

print("Paises em que ja esteve de ferias:")
for vacation in soldier['vacations']:
    print("\t" + vacation.title())
