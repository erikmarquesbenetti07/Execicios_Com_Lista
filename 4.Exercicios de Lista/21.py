# Inicialize as listas para armazenar os modelos e os consumos
modelos = []
consumos = []

# Solicite ao usuário para inserir os modelos e consumos dos carros
for i in range(5):
    modelo = input(f"Veículo {i + 1}\nNome: ")
    km_por_litro = float(input("Km por litro: "))
    modelos.append(modelo)
    consumos.append(km_por_litro)

# Encontre o índice do carro mais econômico
indice_mais_economico = consumos.index(max(consumos))

# Imprima os resultados
print("\nRelatório Final")
for i in range(5):
    litros_para_1000_km = 1000 / consumos[i]
    custo = litros_para_1000_km * 2.25
    print(f"{i + 1} - {modelos[i]} - {consumos[i]} - {litros_para_1000_km:.1f} litros - R$ {custo:.2f}")

print(f"O menor consumo é do {modelos[indice_mais_economico]}.")
