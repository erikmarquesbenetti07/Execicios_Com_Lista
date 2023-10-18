# Inicialize uma lista para armazenar os valores
valores = []

# Inicialize variáveis para cálculos
soma = 0
quantidade = 0
media = 0

# Solicite os valores ao usuário
while True:
    valor = float(input("Digite um valor (ou -1 para encerrar): "))
    if valor == -1:
        break  # Encerra a entrada de dados se -1 for digitado
    valores.append(valor)
    soma += valor
    quantidade += 1

# Mostre a quantidade de valores lidos
print("Quantidade de valores lidos:", quantidade)

# Mostre todos os valores na ordem em que foram informados, um ao lado do outro
print("Valores na ordem original:", end=" ")
for valor in valores:
    print(valor, end=" ")

# Mostre todos os valores na ordem inversa à que foram informados, um abaixo do outro
print("\nValores na ordem inversa:")
for valor in reversed(valores):
    print(valor)

# Mostre a soma dos valores
print("Soma dos valores:", soma)

# Calcule e mostre a média dos valores
if quantidade > 0:
    media = soma / quantidade
print("Média dos valores:", media)

# Calcule e mostre a quantidade de valores acima da média
acima_da_media = sum(1 for valor in valores if valor > media)
print("Quantidade de valores acima da média:", acima_da_media)

# Calcule e mostre a quantidade de valores abaixo de sete
abaixo_de_sete = sum(1 for valor in valores if valor < 7)
print("Quantidade de valores abaixo de sete:", abaixo_de_sete)

# Encerre o programa com uma mensagem
print("Programa encerrado.")
