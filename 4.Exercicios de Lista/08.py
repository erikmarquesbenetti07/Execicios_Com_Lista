# Crie vetores vazios para armazenar as idades e alturas
idades = []
alturas = []

# Use um loop para ler as informações de 5 pessoas
for i in range(5):
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i + 1)))
    altura = float(input("Digite a altura da {}ª pessoa (em metros): ".format(i + 1)))
    idades.append(idade)
    alturas.append(altura)

# Imprima as idades na ordem inversa à ordem lida
print("Idades na ordem inversa:")
for idade in reversed(idades):
    print(idade)

# Imprima as alturas na ordem inversa à ordem lida
print("Alturas na ordem inversa:")
for altura in reversed(alturas):
    print(altura)
