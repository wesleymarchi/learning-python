# Lidando com números

age = 18
print(age == 18)

if age >= 18:
    print('Ainda não recebeu sua carta de Hogwarts?')

if age > 18:
    print('Você tem mais de 18 anos.')
else:
    print('Você tem 18 anos ou menos')

age = 15

if age <= 15:
    print('Você não pode votar.')
else:
    print('Você já pode votar.')

age = 18

if age < 18:
    print('Você não pode dirigir.')
else:
    print('Você já pode tirar sua habilitação.')

x = 1
y = 2

print((x == 1) and (y == 1))
print((x >= y) or (y == 2))