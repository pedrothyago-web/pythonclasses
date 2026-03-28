# ---------------------------------------------------------------------------------------------------------------------------

# Escreva um código que, dado o número de km rodados e o número de horas esperadas parado, calcule a tarifa do taxi

# ---------------------------------------------------------------------------------------------------------------------------

while True:
    periodo = input("Qual o perído do dia (diurno ou noturno): ").lower()

    if periodo == "diurno":
        preco_km = 2.8
        break

    elif periodo == "noturno":
        preco_km = 3.25
        break

    else:
        print("Isso não é um período, tente novamente.")
    

tarifa = 5.5
preco_hora_parada = 44

km_rodados = int(input("Digite quantos km você rodou: "))

horas_esperadas = int(input("Digite quantas horas o motorista te esperou parado: "))
horas_esperadas_total = horas_esperadas * preco_hora_parada

valor = (km_rodados * preco_km) + tarifa
valor_final_dia = valor + horas_esperadas_total
print(f"O valor final da corrida é R${valor_final_dia:.2f}.")