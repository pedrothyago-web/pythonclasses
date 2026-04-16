# Mulheres: 62 anos + 15 anos de contribuição
# Homens: 65 anos + 15 anos de contribuição

def pode_aposentar(sexo, contribuicao, idade):
    if sexo == 'mulher' and (contribuicao < 15 or idade < 62):
        print("mulher que nao pode aposentar")
        return False
    if sexo == 'homem' and (contribuicao < 15 or idade < 65):
        print("homem que nao pode aposentar")
        return False
    return True

assert (pode_aposentar("mulher", 10, 70) == False)
assert (pode_aposentar("mulher", 20, 70) == True)
assert (pode_aposentar("homem", 20, 50) == False)
assert (pode_aposentar("homem", 12, 70) == False)
assert (pode_aposentar("homem", 17, 70) == True)