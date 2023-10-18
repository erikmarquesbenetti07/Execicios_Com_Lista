# Crie um vetor vazio para armazenar os números
vetor = []

# Use um loop para ler os 5 números e adicioná-los ao vetor
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

# Mostre os números armazenados no vetor
print("Os números digitados são:")
for numero in vetor:
    print(numero)
