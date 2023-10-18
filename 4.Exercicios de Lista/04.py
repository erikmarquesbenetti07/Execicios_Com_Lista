# Crie um vetor vazio para armazenar os caracteres
vetor = []

# Use um loop para ler os 10 caracteres e adicioná-los ao vetor
for i in range(10):
    caractere = input("Digite um caractere: ")
    vetor.append(caractere)

# Crie uma lista de consoantes
consoantes = "bcdfghjklmnpqrstvwxyz"

# Inicialize uma variável para contar as consoantes
count_consoantes = 0

# Crie uma lista para armazenar as consoantes lidas
consoantes_lidas = []

# Verifique cada caractere no vetor e conte as consoantes
for caractere in vetor:
    if caractere.lower() in consoantes:
        count_consoantes += 1
        consoantes_lidas.append(caractere)

# Imprima as consoantes e a contagem
print("Consoantes lidas:")
for consoante in consoantes_lidas:
    print(consoante)

print("Total de consoantes lidas:", count_consoantes)
