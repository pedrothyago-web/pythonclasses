# Ler um ano, e criar 3 variáveis:
# esta_no_passado
# esta_no_futuro
# esta_no_presente

 
ano = int(input("Digite o ano em que você está: "))

if ano >= 2027:
    print("Você está no futuro!")

elif ano <= 2025:
    print("Você está no passado!")

else:
    print("Você está no presente!")
    