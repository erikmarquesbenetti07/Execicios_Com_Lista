# Crie uma lista vazia para armazenar as temperaturas médias mensais
temperaturas_mensais = []

# Crie uma lista para armazenar os nomes dos meses por extenso
meses_extenso = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Use um loop para ler as temperaturas médias de cada mês
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses_extenso[i]}: "))
    temperaturas_mensais.append(temperatura)

# Calcule a média anual das temperaturas
media_anual = sum(temperaturas_mensais) / 12

# Encontre e mostre as temperaturas acima da média anual
print("Meses com temperatura acima da média anual:")
for i in range(12):
    if temperaturas_mensais[i] > media_anual:
        print(f"{meses_extenso[i]} - {temperaturas_mensais[i]}°C (acima da média anual)")

print(f"A média anual de temperaturas é {media_anual}°C.")
