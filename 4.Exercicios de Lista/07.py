# Crie um vetor vazio para armazenar os números
vetor = []

# Use um loop para ler os 5 números e adicioná-los ao vetor
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

# Calcule a soma e a multiplicação dos números
soma = sum(vetor)
multiplicacao = 1
for numero in vetor:
    multiplicacao *= numero

# Mostre os números, a soma e a multiplicação na tela
print("Números digitados:", vetor)
print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)
