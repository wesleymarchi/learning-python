# Ordenando uma lista com sort() - permanente

heros = ['batman', 'superman', 'spiderman', 'rorschach']
heros.sort()  # ordena em ordem alfabetica

print(heros)

# Ordena de forma reversa
heros.sort(reverse=True)
print(heros)

# Ordena mas mantém a lista original
print(sorted(heros))

# Apenas exibe a lista de forma inversa - sem ordenação
print(heros.reverse())
