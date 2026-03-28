# ---------------------------------------------------------------------------------------------------------------------------

# Escreva um código que recebe um ano e imprime:
# Ano de olimpiada
# Ano de copa
# Ano sem evento
# ---------------------------------------------------------------------------------------------------------------------------
# a lógica é, se o resto da divisão por 4 for:
# 0 = olimpiada, 
# 2 = copa
# 3 e 1 = sem evento.
# ---------------------------------------------------------------------------------------------------------------------------

year = int(input("In which year would you like to check the events?: "))

if year % 4 == 0:
    print("There are Olympics this year.")

elif year % 4 == 2:
    print("There's a World Cup this year.")

else:
    print("There are no events this year.")