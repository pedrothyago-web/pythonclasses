# Escreva um código que recebe uma idade. 
# Se você pode, mas nao precisa votar, ele imprime “Pode mas nao precisa”
# Se você precisa votar, ele imprime “Precisa”
# Se você não pode votar, ele imprime “nao pode”
# ----------------------------------------------------------------------------

# age = int(input("How old are you?: "))

# if age < 16:
#         print("You can't vote.")

# elif (age >= 16 and age < 18) or (age >= 70 ):
#     print("You can vote, but it's optional.")

# elif (age >= 18) and (age < 70):
#     print("You need to vote.") 


# ---------------------------------------------------------------------------- 
# jogando dentro de uma função e utilizando (puxando) ela lá em baixo

def needvote(age):

    if (age >= 16 and age < 18) or (age >= 70 ):
        print("You can vote, but it's optional.")

    elif (age >= 18) and (age < 70):
        print("You need to vote.")

    else:
        print("You can't vote.")

needvote(60) #need
needvote(18) #need
needvote(15) #cant vote
needvote(17) #can vote, but its optional #a

# -------------------------------------

