# ---------------------------------------------------------------------------------------------------------------------------

#Dada uma dívida, um juros e um número de meses, dizer quanto é a dívida final

#j = c * i * t 
#j = juros
#c = capital inicial
#i = taxa de juros mensal (em decimal)
#t = tempo em meses

# ---------------------------------------------------------------------------------------------------------------------------

divida = int(input("Qual o valor da sua dívida?: "))
juros = int(input("Qual o valor do juros?: "))
meses = int(input("Qual a quantidade de meses?: "))


juros_d = juros / 100 #transformar em decimal

divida_final = (divida * juros_d * meses) + divida

print(f"A sua dívida final é: R${divida_final:.2f}")
11