# Crie três vetores vazios para armazenar os números, pares e ímpares
numeros = []
PAR = []
impar = []

# Use um loop para ler os 20 números e adicioná-los ao vetor "numeros"
for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Separe os números em pares e ímpares
for numero in numeros:
    if numero % 2 == 0:
        PAR.append(numero)
    else:
        impar.append(numero)

# Imprima os três vetores
print("Números digitados:", numeros)
print("Números pares:", PAR)
print("Números ímpares:", impar)
