# Inicialize variáveis para o nome e os saltos do atleta
nome_atleta = input("Digite o nome do atleta (ou pressione Enter para encerrar): ")

while nome_atleta != "":
    saltos = []

    # Use um loop para ler os cinco saltos
    for i in range(5):
        salto = float(input(f"Digite a distância do {i + 1}º salto em metros: "))
        saltos.append(salto)

    # Calcule a média dos saltos
    media_saltos = sum(saltos) / len(saltos)

    # Imprima as informações
    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print("Saltos:", " - ".join([f"{salto} m" for salto in saltos]))
    print(f"Média dos saltos: {media_saltos} m\n")

    # Solicite o nome do próximo atleta
    nome_atleta = input("Digite o nome do próximo atleta (ou pressione Enter para encerrar): ")

print("Programa encerrado.")

