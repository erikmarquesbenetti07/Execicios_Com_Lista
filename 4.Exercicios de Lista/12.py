# Inicialize listas vazias para armazenar idades e alturas dos alunos
idades = []
alturas = []

# Defina o número de alunos
num_alunos = 30

# Use um loop para ler as idades e alturas dos alunos
for i in range(num_alunos):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = float(input(f"Digite a altura do aluno {i + 1} (em metros): "))
    idades.append(idade)
    alturas.append(altura)

# Calcule a média de altura dos alunos
media_altura = sum(alturas) / num_alunos

# Inicialize uma variável para contar os alunos com mais de 13 anos e altura inferior à média
alunos_contados = 0

# Verifique as condições para cada aluno
for i in range(num_alunos):
    if idades[i] > 13 and alturas[i] < media_altura:
        alunos_contados += 1

# Imprima o resultado
print(f"Quantidade de alunos com mais de 13 anos e altura inferior à média: {alunos_contados}")
