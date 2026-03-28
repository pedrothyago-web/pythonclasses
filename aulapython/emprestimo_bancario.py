# ---------------------------------------------------------------------------------------------------------------------------

# Exercício: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

# ---------------------------------------------------------------------------------------------------------------------------

valor_casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos para pagar: "))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

print(f"Prestação mensal: R$ {prestacao:.2f}")

if prestacao <= limite:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")
    