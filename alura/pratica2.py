# # Coletamos os valores de início e fim
# inicio = int(input('Insira o primeiro número inteiro: '))
# fim = int(input('Insira o segundo número inteiro: '))

# # Verificamos se o valor de início é maior que o fim
# if inicio < fim:
#   # podemos imprimir os inteiros entre o menor e o maior valor
#     for i in range(inicio + 1, fim): 
#      print(i)
# elif inicio > fim:
#     for i in range(fim + 1, inicio):
#      print(i)
# else: #caso os números sejam iguais, não conseguimos imprimir sequência alguma
#   print('Os números são iguais.')


colonia_a = 4 
colonia_b = 10

taxa_a = 0.03
taxa_b = 0.01

dias = 0

while colonia_a <= colonia_b:
    colonia_a *= 1 + taxa_a
    colonia_b *= 1 + taxa_b

    dias += 1

print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')
