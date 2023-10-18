# Crie um vetor vazio para armazenar os números
vetor_A = []

# Use um loop para ler os 10 números inteiros e adicioná-los ao vetor
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor_A.append(numero)

# Inicialize uma variável para a soma dos quadrados
soma_quadrados = 0

# Calcule a soma dos quadrados dos elementos do vetor
for numero in vetor_A:
    soma_quadrados += numero ** 2

# Mostre a soma dos quadrados
print("A soma dos quadrados dos elementos do vetor é:", soma_quadrados)
