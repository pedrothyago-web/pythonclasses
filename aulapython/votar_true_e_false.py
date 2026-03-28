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