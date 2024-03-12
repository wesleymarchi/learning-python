# Definindo palavras em maiúsculas e minúsculas

first_name = "wesley"
last_name = "marchi"

print("Primeira letra maiúscula: ")
print(first_name.title() + " " + last_name.title())

print("\nMaiúscula: ")  # caractere de escape
print(first_name.upper() + " " + last_name.upper())

print("\nMinúscula: ")
print(first_name.lower() + " " + last_name.lower())

# concatenação dos nomes
full_name = first_name + " " + last_name
print("\nConcatenação: ")
print(full_name.title())