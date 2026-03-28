# ---------------------------------------------------------------------------------------------------------------------------

# Escreva um programa para determinar se uma pessoa deve ou não pagar imposto, considerando seu salário mensal – procure no google o salário anual mínimo que exige o pagamento de imposto

# ---------------------------------------------------------------------------------------------------------------------------

mensal_salary = float(input("Insert your mensal salary: R$ "))

if mensal_salary <= 5000:
    print("no need to pay tax")

else:
    print("need to pay tax")