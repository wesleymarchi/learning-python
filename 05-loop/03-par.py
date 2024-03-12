# Utilize operador de módulo para definir se um numero é impar ou par

x = input("Insira um numero...\n")
x = int(x)

if x % 2 == 0:
    print(str(x) + " é um numero par.")
else:
    print(str(x) + " é impar.")
