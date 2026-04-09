def calcularIdade(nome, ano_nascimento):
    idade = 2026 - ano_nascimento
    print(f'A pessoa {nome} tem a idade {idade}')
    return idade 

first_person = calcularIdade('Pedro',2005)
second_person = calcularIdade('Joao', 2010)
thrid_person = calcularIdade('Daniel',2001)    


#outro exemplo: 

def calcularpreco (nome, gramas):
    preco = gramas * 3.00
    print(f'O preco do produto é {preco}')
    return preco 

produtoOne = calcularpreco ('Abacate', 100)
produtosecond = calcularpreco ('Morango', 182)
produtoThird = calcularpreco ('Tomate', 102.5)


# hard instance: 
#Escreva uma função que recebe o ano de nascimento da pessoa e retorna a idade atual da pessoa (em 2026)

def calcularIdade(nome, ano_nascimento, fez_aniversario):
    idade = 2026 - ano_nascimento 
    if not fez_aniversario: #fez-aniversario == false
        idade = idade - 1 
        print(f"A pessoa {nome} tem a idade {idade}")
    return idade 

pessoa1 = calcularIdade ("Joao", 2004)
pessoa1 = calcularIdade ("mateus", 2001)
pessoa1 = calcularIdade ("Pedro", 2002)


#outro exemplo: 

#Escreva uma função que recebe uma velocidade (em km/h) e o quilometro atual dele na estrada, e retorne a posição do carro na estrada daqui a duas horas

def posicao(km_atual, velocidade):
    nova_posicao = velocidade + km_atual *2
    return nova_posicao 

a = posicao(100,20) #tem que dar 140
assert a == 140
b = posicao(50,100) #tem que dar 250
assert b == 250
c = posicao(100,120) #tem que dar 340
assert c == 340