# Crie um vetor vazio para armazenar os números
vetor = []

# Use um loop para ler os 10 números e adicioná-los ao vetor
for i in range(10):
    numero = float(input("Digite um número real: "))
    vetor.append(numero)

# Mostre os números na ordem inversa
print("Os números em ordem inversa são:")
for i in range(9, -1, -1):
    print(vetor[i])
