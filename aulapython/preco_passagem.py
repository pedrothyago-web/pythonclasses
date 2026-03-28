# ---------------------------------------------------------------------------------------------------------------------------

# Exercício: Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km (inclusive o 200), e R$0,45 para viagens mais longas

# ---------------------------------------------------------------------------------------------------------------------------

km = int(input("How many kilometers do you want to travel?: "))

#dúvida, como faço para deixar essa variavel (já que ela nao muda) fora do else? (trip = km * km_value)

if km <= 200: #se for menor de 200km
    km_value = 0.50
    trip = km * km_value

    print(f"The final cost of your trip is ${trip:.2f}.")

else:
    km_value = 0.45
    trip = km * km_value

    print(f"The final cost of your trip is ${trip:.2f}.")