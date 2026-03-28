# ---------------------------------------------------------------------------------------------------------------------------

# Recebe um nome e uma idade, faz um print do tipo
# “lucas pode votar”
# e retorna True (se a pessoa pode votar) e False (caso contrário)

# ---------------------------------------------------------------------------------------------------------------------------


def podevotar(nome, idade):
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar.")
        return True
    else: 
        print(f"Não, a pessoa {nome} não pode votar.")
        return False

a = podevotar("Matheus", 38)
print(f"A primeira resposta é {a}.\n")

b = podevotar("Pedro", 14)
print(f"A primeira resposta é {b}.")


# -----------------------------------------------------------------------------------

#if decide rodar ou nao determinado codigo baseado no true or false de um bool
#27/03

a = 12
b = 15
if a > b: #essa comparacao vale True ou False dependendo
          #dos valores de a e b. Se valer True, vou executar as duas 
          #linhas espaçadas “dentro do if”
   print("o maior numero é", a)
   maior = a
else:    #Se valer False, vou executar as duas 
         #linhas espaçadas “dentro do else”
   print(a, "não é o maior")


# nas linhas (45-48) não vai excutar porque a deve ser maior que b, alem disso tambem é um false e para ser executado deve ser true.
# Ou seja, será executado 12 não é maior.


# -------------------------------------------------
if True: # dessa vez, coloquei direto um booleano, o else jamais será
        # executado
   print("o maior numero é", a)
else:
   print(a, "não é o maior")         # jamais vai rodar

 # -------------------------------------------------

a = 12
b = 15
if a > b: #essa comparacao vale True ou False dependendo
          #dos valores de a e b. Se valer True, vou executar as duas 
          #linhas espaçadas “dentro do if”
   print("o maior numero é", a)
   maior = a
elif a < b:
     print("o maior numero é", a)
     maior = a
else:    #Se valer False, vou executar as duas 
         #linhas espaçadas “dentro do else”
   print(a, "não é o maior")