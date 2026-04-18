#É possivel executar um mesmo código para cada elemento de uma lista

# lista_alunos = ["Jose Augusto", "Jose Pina", "Cristina" ]
# qtd = 0

# for aluno in lista_alunos:
#    print("nome do aluno", aluno)      
#    qtd = qtd + 1                 
#    print("esse eh o aluno", qtd) 



# lista_alunos = ["Zé", "Pina", "Cris"]
# ultimo = lista_alunos[len(lista_alunos)-1]
# print(len(lista_alunos), ultimo)
# print(len(lista_alunos))
# lista_alunos.append("Hello")  #funçao para adicionar um argumento. 
# print(len(lista_alunos))
# lista_alunos[0] = "josé"

#---------------------------------------------------------------

def primeiro(lista): 
    pass 

lista_chamada = ("numero 1", "numero 2", "numero 3", "numero 4")
primeiro = lista_chamada[0]

def ultimo(lista):
    pass

lista_objetos = ("borracha", "tesoura", "caderno")  
ultimo = lista_objetos [len(lista_objetos)-1]
print(len(lista_objetos), ultimo)


def maior_valor(lista):
    maior_Valor = 0 
    for e in lista: 
        if e > maior_Valor: 
            maior_Valor = e 
    return maior_Valor
