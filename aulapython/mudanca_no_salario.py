# ---------------------------------------------------------------------------------------------------------------------------

# O sindicato de programadores fez o seguinte acordo com a empresa: as pessoas que ganham salários menores que 4000 reais terão aumento de 15%, as demais, aumento de 10%. Escreva um código que pede o valor do salário (permitindo casas decimais) e calcula o novo valor

# ---------------------------------------------------------------------------------------------------------------------------

salary = float(input("What is your salary?: "))

if salary <= 4000:
    salary *= 1.15
    print(f"Your new salary is: ${salary:.2f}")

else:
    salary *= 1.1
    print(f"Your new salary is: ${salary:.2f}")