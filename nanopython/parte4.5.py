# Ler um número, e criar três variáveis:
# eh_positivo
# eh_negativo
# eh_zero


number = int(input("Write a number: "))

if number <= -1:
    print("This number is negative.")

elif number >= 1:
    print("This number is positive.")

else:
    print("It's zero.")