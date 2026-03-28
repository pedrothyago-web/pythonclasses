# ---------------------------------------------------------------------------------------------------------------------------

# dada uma velocidade, imprima as multas baseado nos valores reais (pontos na cnh também)

# Até 20% acima do limite permitido: R$ 130,16 e 4 pontos na CNH
#De 20% até 50% acima do limite permitido: R$ 195,23 e 5 pontos na CNH
# Acima de 50% do limite permitido: R$ 880,41 e Suspensão da CNH

# ---------------------------------------------------------------------------------------------------------------------------

speed = int(input("At what speed did you pass the radar? (km/h): "))

max_speed = 80 #km/h


if speed <= max_speed:
    print("You are within the speed limit.")

elif (speed >= 81) and (speed <= 96): #até 20% 
    print("You received a fine of R$130,16 and 4 points on your driver's license.")

elif (speed >= 96) and (speed <= 120): #20% a #50%
    print("You received a fine of R$195,23 and 5 points on your driver's license.")

else: #acima de 50
    print("You received a fine of R$880,41 and had your driver's license suspended.")