# Inputs numericos

prompt = input("Quantos anos você tem?\n")
print("Sem utilizar a função int(): " + prompt)

prompt = int(prompt)

print("Resposta utilizando int(): " + str(prompt))

if prompt >= 18:
    print("Parabéns, você já pode tirar sua CNH.")
else:
    print("Você ainda não pode tirar a CNH.")
