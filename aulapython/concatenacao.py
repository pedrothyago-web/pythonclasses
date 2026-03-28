# ---------------------------------------------------------------------------------------------------------------------------

# Exercício: Faça um programa que dado dois nomes (em minúsculo) retorne a concatenação deles, em ordem alfabética, com um “e” no meio. Exemplo: de ‘helder’ e  ‘maria’ teremos ‘helder e maria’

# ---------------------------------------------------------------------------------------------------------------------------

name1 = input("What are the first name?: ").lower()
name2 = input("What are the second name?: ").lower()

concatenation = name1 + " and " + name2

print(f"The combination of the two names is: {concatenation}")
