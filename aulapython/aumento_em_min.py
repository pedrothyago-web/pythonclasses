# ---------------------------------------------------------------------------------------------------------------------------

# Dada uma quantidade de minutos e um aumento em minutos, dizer qual o próximo valor dos minutos (depois a gente pensa na hora!)

# ---------------------------------------------------------------------------------------------------------------------------

minutos = int(input("Digite a quantidade de minutos: "))

print("A quantidade de minutos é: ", minutos)
aumento_em_min = int(input("Digite o aumento dos minutos: "))

min_total = minutos + aumento_em_min

if min_total >= 60:
    horas = min_total // 60 #divisão inteira (ex 125 // 60 = 2)
    minutos = min_total % 60 #serve para descobrir os min que sobraram depois de formar as horas.
    print(f"{horas}h e {minutos}min")

else:
    print(f"A quantidade de minutos total é: {min_total} minutos")