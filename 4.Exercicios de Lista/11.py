# Crie três vetores vazios para armazenar os elementos dos três vetores iniciais
vetor1 = []
vetor2 = []
vetor3 = []

# Use loops para ler os 10 elementos de cada vetor
for i in range(10):
    elemento1 = int(input(f"Digite o {i+1}º elemento do primeiro vetor: "))
    vetor1.append(elemento1)

for i in range(10):
    elemento2 = int(input(f"Digite o {i+1}º elemento do segundo vetor: "))
    vetor2.append(elemento2)

for i in range(10):
    elemento3 = int(input(f"Digite o {i+1}º elemento do terceiro vetor: "))
    vetor3.append(elemento3)

# Crie um vetor vazio para armazenar os elementos intercalados dos três vetores
vetor_resultante = []

# Intercale os elementos dos três vetores no vetor resultante
for i in range(10):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])
    vetor_resultante.append(vetor3[i])

# Imprima o vetor resultante com os elementos intercalados
print("Vetor resultante com elementos intercalados:", vetor_resultante)
