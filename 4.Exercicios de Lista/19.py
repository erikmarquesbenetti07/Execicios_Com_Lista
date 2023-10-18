# Inicialize um dicionário para armazenar os votos para cada sistema operacional
votos = {
    "Windows Server": 0,
    "Unix": 0,
    "Linux": 0,
    "Netware": 0,
    "Mac OS": 0,
    "Outro": 0
}

while True:
    print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?")
    print("Escolha uma opção (1 a 6) ou 0 para encerrar a enquete.")
    
    voto = input("Voto: ")
    
    if voto == "0":
        break
    elif voto in ["1", "2", "3", "4", "5", "6"]:
        opcoes = list(votos.keys())
        votos[opcoes[int(voto) - 1]] += 1
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

total_votos = sum(votos.values())

print("Sistema Operacional     Votos   %")
print("-------------------     -----   ---")

for sistema, num_votos in votos.items():
    percentual = (num_votos / total_votos) * 100
    print(f"{sistema:25} {num_votos:7} {percentual:.1f}%")

print("-------------------     -----")
print(f"Total{total_votos:18}")

vencedor = max(votos, key=votos.get)
percentual_vencedor = (votos[vencedor] / total_votos) * 100

print(f"O Sistema Operacional mais votado foi o {vencedor}, com {votos[vencedor]} votos, correspondendo a {percentual_vencedor:.1f}% dos votos.")
