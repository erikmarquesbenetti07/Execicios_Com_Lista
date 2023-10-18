# Crie uma lista vazia para armazenar as notas
notas = []

# Use um loop para ler as 4 notas e adicioná-las à lista
for i in range(4):
    nota = float (input("Digite a {}ª nota: ".format(i + 1)))
    notas.append(nota)

# Calcule a média das notas
media = sum(notas) / 4

# Mostre as notas e a média na tela
print("Notas digitadas:")
for i, nota in enumerate(notas, start=1):
    print("Nota {}: {}".format(i, nota))

print("Média das notas: {:.2f}".format(media))
