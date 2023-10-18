# Crie um vetor vazio para armazenar as médias dos alunos
medias = []

# Defina um limite para a média desejada (7.0)
limite_media = 7.0

# Use um loop para ler as notas e calcular as médias
for aluno in range(10):
    notas = []  # Crie um vetor para armazenar as notas do aluno
    for i in range(4):
        nota = float(input(f"Informe a nota {i + 1} do aluno {aluno + 1}: "))
        notas.append(nota)
    
    # Calcule a média do aluno e adicione ao vetor de médias
    media = sum(notas) / 4
    medias.append(media)

# Conte o número de alunos com média maior ou igual a 7.0
alunos_aprovados = sum(1 for media in medias if media >= limite_media)

# Imprima o número de alunos aprovados
print(f"Número de alunos com média maior ou igual a {limite_media}: {alunos_aprovados}")
