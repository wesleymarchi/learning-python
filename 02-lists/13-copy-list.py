# Copiando uma lista

heros = ['batman', 'superman', 'spiderman', 'rorschach']

"""
lista = heros
print("Lista copiada: ", lista)
lista.append('mulher maravilha')
print("Heros: ", heros)
"""

copy_heros = heros[:]  # Copia a lista original

copy_heros.append('joker')

print(heros)
print(copy_heros)
print(heros)
