# Inicialize variáveis
salarios = []
abonos = []
total_colaboradores = 0
total_abono = 0
colaboradores_minimo = 0

# Solicite os salários até que seja inserido um salário igual a 0
while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    salarios.append(salario)

# Calcule o abono e mantenha o controle de várias estatísticas
for salario in salarios:
    abono = salario * 0.20
    if abono < 100:
        abono = 100
        colaboradores_minimo += 1
    abonos.append(abono)
    total_colaboradores += 1
    total_abono += abono

# Encontre o maior valor de abono
maior_abono = max(abonos)

# Exiba os salários e abonos
print("\nProjeção de Gastos com Abono")
print("============================\n")

for i in range(total_colaboradores):
    print(f"Salário: R$ {salarios[i]:.2f} - Abono: R$ {abonos[i]:.2f}")

# Exiba as estatísticas finais
print(f"\nForam processados {total_colaboradores} colaboradores")
print(f"Total gasto com abonos: R$ {total_abono:.2f}")
print(f"Valor mínimo pago a {colaboradores_minimo} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono:.2f}")
