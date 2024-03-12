matriz = []  # matriz vazia

tll = int(input("Digite o tamanho logico da linha: "))
tlc = int(input("Digite o tamanho logico da coluna: "))

for i in range(tll):
    linha = []
    for j in range(tlc):
        linha.append(int(input("Insira um valor: ")))

    matriz.append(linha)

print(matriz)

for linha in matriz:
    print(linha)

row = int(input("Digite a linha desejada: ")) - 1
col = int(input("Digite a coluna desejada: ")) - 1

print(matriz[row][col])
