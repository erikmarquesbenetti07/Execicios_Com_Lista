def calcular_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100

def main():
    votos = [0] * 24  # Inicializa um array de votos com 24 elementos (índices de 0 a 23)
    total_votos = 0

    while True:
        numero_jogador = int(input("Número do jogador (0=fim): "))
        
        if numero_jogador == 0:
            break
        
        if 1 <= numero_jogador <= 23:
            votos[numero_jogador] += 1
            total_votos += 1
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")

    with open("resultado_votacao.txt", "w") as arquivo:
        arquivo.write("Resultado da votação:\n\n")
        arquivo.write(f"Foram computados {total_votos} votos.\n\n")
        arquivo.write("Jogador  Votos    %\n")
        
        melhor_jogador = None
        melhor_votos = 0

        for jogador, votos_jogador in enumerate(votos):
            if votos_jogador > 0:
                percentual = calcular_percentual(votos_jogador, total_votos)
                arquivo.write(f"{jogador:<8} {votos_jogador:<8} {percentual:.1f}%\n")
                
                if votos_jogador > melhor_votos:
                    melhor_jogador = jogador
                    melhor_votos = votos_jogador
        
        arquivo.write(f"\nO melhor jogador foi o número {melhor_jogador}, com {melhor_votos} votos, correspondendo a {calcular_percentual(melhor_votos, total_votos):.1f}% do total de votos.")
    
    print("Resultado da votação gravado em 'resultado_votacao.txt'.")

if __name__ == "__main":
    main()
