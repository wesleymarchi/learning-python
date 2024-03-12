# Exibe uma sequência de números

for value in range(1, 6):  # range gera uma sequencia de números
    print(value)

# Define uma lista de números
numbers = list(range(1, 6))
print(numbers)

# Define uma lista com números pares
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Definindo o quadrado da lista
squares = []  # lista vazia
for value in range(1, 11):
    square = value**2
    squares.append(square) # Concatena square na lista

print(squares)

# list comprehensions
new_list = [value**2 for value in range(1, 11)]
print(new_list)
