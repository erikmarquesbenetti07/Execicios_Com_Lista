# Função para converter bytes em megabytes
def bytes_to_megabytes(bytes):
    return bytes / (1024 * 1024)

# Função para calcular o percentual de uso
def percentual_uso(espaco, espaco_total):
    return (espaco / espaco_total) * 100

# Ler o arquivo "usuarios.txt" e armazenar os dados em uma lista
with open("usuarios.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# Inicializar listas para armazenar os nomes e espaços em disco
nomes = []
espacos = []

# Processar as linhas e extrair nomes e espaços em disco
for linha in linhas:
    partes = linha.split()
    nome = partes[0]
    espaco = int(partes[1])
    nomes.append(nome)
    espacos.append(espaco)

# Calcular o espaço total ocupado e o espaço médio ocupado
espaco_total = sum(espacos)
espaco_medio = espaco_total / len(nomes)

# Abrir o arquivo "relatório.txt" para escrever os resultados
with open("relatório.txt", "w") as relatorio:
    relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    relatorio.write("------------------------------------------------------------------------\n")
    relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")

    for i, nome in enumerate(nomes, start=1):
        espaco_em_mb = bytes_to_megabytes(espacos[i - 1])
        percentual = percentual_uso(espacos[i - 1], espaco_total)
        relatorio.write(f"{i:<4} {nome:<15} {espaco_em_mb:10.2f} MB {percentual:10.2f}%\n")

    relatorio.write(f"\nEspaço total ocupado: {bytes_to_megabytes(espaco_total):.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {espaco_medio:.2f} MB\n")

print("Relatório gerado com sucesso e salvo em 'relatório.txt'.")
