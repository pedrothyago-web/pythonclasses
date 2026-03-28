# Juntando booleanos
# Em muitos casos, precisamos juntar mais de um booleano para chegar a uma conclusão. Para isso, temos os operadores lógicos: and, or e not.
# and: verdadeiro se ambos os booleanos forem verdadeiros
# or: verdadeiro se pelo menos um dos booleanos for verdadeiro
# not: inverte o valor do booleano

usuario_tem_permisao = True
senha_correta = True
biometria_valida = False # o sistema de segurança falhou, a biometria não é valida, o acesso é negado (false)

acesso_permitido = usuario_tem_permisao and senha_correta and biometria_valida # o acesso só é permitido se os tres forem verdadeiros, se um deles for falso, o acesso é negado (false)
print("=== sistema de segurança===")
print(f"Usuario tem permissao: {usuario_tem_permisao}")
print(f"Senha Correta: {senha_correta}")
print(f"Biometria valida: {biometria_valida}")
print(f"Acesso permitido: {acesso_permitido}")
      


# AND (duas portas, mas precisamos atravessar todas elas) ou seja, basta um false para gerar um false (true/false = false) (false/false = false) (true/true = true)
# se houver um false se torna false (true/false = false)


# OR (duas portas, mas só precisamos atravessar uma delas) ou seja, basta um true para gerar um true (true/false = true) (true/true = true)
# se ambos forem false, se torna false (false/false = false)
tem_dinheiro = True
tem_cartao = False

pode_comprar = tem_dinheiro or tem_cartao # basta um deles ser verdadeiro para que possa comprar (true/false = true) (false/false = false) (true/true = true)
print(f"Pode comprar? {pode_comprar}")


#not (so inverte o valor)

#Exercício: Faça um programa que retorne verdadeiro ou falso sobre sua aprovação na disciplina, considerando a presença (um numero de 0 a 100, indicando a porcentagem de presença) e a nota (de 0 a 10)
# para ser aprovado, o aluno precisa ter nota maior ou igual a 6 e presença maior ou igual a 75%

nota = 3.0
presenca = 76

aprovado    =    (nota >= 6) and (presenca >= 75) # para ser aprovado, o aluno precisa ter nota maior ou igual a 6 e presença maior ou igual a 75%
reprovado   =    (nota < 4)  or  (presenca < 75) # para ser reprovado, o aluno precisa ter nota menor que 4 ou presença menor que 75%
exame       =    (nota >= 4) and (nota < 6) and (presenca >= 75) #opcao 1 para exame, o aluno precisa ter nota maior ou igual a 4 e menor que 6 e presença maior ou igual a 75%
exame       =    (     4 <= nota < 6      ) and (presenca >= 75) #opcao 2(somente no python) 
exame       =    (not aprovado) and (not reprovado) # opcao 3


# votar: pode, pode, tem que, pode
# dada idade de uma pessoa, crie os seguintes booleanos: 
# pessoa pode entrar na cabine e votar (direito_voto)
# pessoa tem a obrigação de votar (obrigacao_voto)
# pessoa tem o voto, mas opcional (voto_opcional)


idade = int(input("Qual sua idade?: ")) # o input retorna uma string, por isso precisamos converter para inteiro usando int()

if idade < 16: # se a idade for menor que 16, a pessoa não pode votar
        print("Você não pode votar.")

elif (idade >= 16 and idade < 18) or (idade >= 70 ): # se a idade for maior ou igual a 16 e menor que 18, ou se a idade for maior ou igual a 70, a pessoa tem o voto opcional
    print("Você pode votar, mas não é obrigatorio.")

elif (idade >= 18) and (idade < 70): # se a idade for maior ou igual a 18 e menor que 70, a pessoa tem a obrigação de votar
    print("Você precisa votar.")