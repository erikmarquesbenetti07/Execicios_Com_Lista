# Crie uma lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Inicialize uma variável para contar respostas positivas
respostas_positivas = 0

# Use um loop para fazer as perguntas e contar as respostas positivas
for pergunta in perguntas:
    resposta = input(pergunta + " (Responda Sim ou Não): ").strip().lower()
    if resposta == "sim":
        respostas_positivas += 1

# Classifique a pessoa com base nas respostas
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Imprima a classificação
print("Classificação: " + classificacao)
