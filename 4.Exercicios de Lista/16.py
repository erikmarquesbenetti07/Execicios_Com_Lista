# Inicialize uma lista de contadores para cada intervalo salarial
contadores = [0] * 10

# Solicite ao usuário o número de vendedores
num_vendedores = int(input("Digite o número de vendedores: "))

# Use um loop para ler os salários e atualizar os contadores
for i in range(num_vendedores):
    salario = float(input(f"Digite o salário do vendedor {i + 1}: "))
    indice = int((salario - 200) / 100)  # Calcula o índice com base no salário
    if indice < 0:
        indice = 0
    elif indice > 9:
        indice = 9
    contadores[indice] += 1

# Imprima o número de vendedores em cada intervalo salarial
intervalos = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599", "$600 - $699",
             "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]
for i in range(10):
    print(f"Vendedores no intervalo {intervalos[i]}: {contadores[i]}")
