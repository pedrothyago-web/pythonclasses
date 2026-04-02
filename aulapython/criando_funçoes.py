#Para organizar o nosso código, chamar ele várias vezes, e testar ele mais fácil, usamos funções

def soma(a, b):    #qeur dizer: vai ter uma função chamada soma e vai precisar de um A e de um B. 
   resultado = a + b  # linha1
   return resultado  # linha2

a = soma(10, 20)
b = soma(20, 30) 
c = soma(10, 12)



# Outro exemplo 

def soma(a, b):  # a e b são argumentos, vão ser atribuidos fora da função 
   resultado = a + b 
   return resultado  

# Toda essa estrutura se chama (ESCOPO). 

def soma(a, b):
   resultado = a + b  # linha1
   return resultado  # linha2

a = soma(10, 20)
b = soma(20, 30)   # quando eu executar essa linha,
# vou ter duas variaveis a. Uma no escopo da funcao soma
# (a caixinha da funcao soma) e a outra no escopo (caixinha) global
c = soma(10, 12) 


# Função RETURN

def soma(a, b):
   resultado = a + b  # linha1
   return resultado  # linha2


a = soma(10, 20)   #30  escrevi o valor de retorno, terei a = 30
b = soma(20, 30) +5 #50   escrevi o valor de retorno no lugar da chamada de função, terei b = 55
c = soma(10, 12) +3 #22    escrevi o valor de retorno no lugar da chamada de função, terei c = 66
