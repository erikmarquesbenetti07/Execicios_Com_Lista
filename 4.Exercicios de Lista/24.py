import random

# Inicialize um vetor de contadores com zeros para cada valor de dado (1 a 6)
contadores = [0] * 6

# Simule o lançamento do dado 100 vezes
for _ in range(100):
    resultado = random.randint(1, 6)  # Gere um número aleatório de 1 a 6
    contadores[resultado - 1] += 1  # Atualize o contador correspondente

# Exiba o número de vezes que cada valor foi obtido
for i in range(6):
    print(f"O valor {i + 1} foi obtido {contadores[i]} vezes.")
