# Removendo espaços em branco

hero = " Iron Man "
print("Original string: " + hero)

print("Remove espaço do lado direito: ")
print(hero.rstrip())

print("Remove espaço do lado esquerdo: ")
print(hero.lstrip())

print("Remove espaço de ambos os lados: ")
print(hero.strip())
