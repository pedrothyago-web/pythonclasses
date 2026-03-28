# ---------------------------------------------------------------------------------------------------------------------------

#dado um valor em segundos, expresse ele usando horas, min e segundos

# ---------------------------------------------------------------------------------------------------------------------------

segundos = int(input("Digite a quantidade de segundos: "))

horas = segundos / 3600
print(f"{segundos} segundo(s) é: {horas:.4f} horas")

minutos = segundos / 60
print(f"{segundos} segundo(s) é: {minutos:.2f} minutos")



