# Tuplas são imutaveis

dimensions = (200, 100)

print(dimensions[0])
print(dimensions[1])

# Loop em uma tupla
for dimension in dimensions:
    print((dimension))

# Sobrescrevendo
dimensions = (10, 20)
for dimension in dimensions:
    print(dimension)
