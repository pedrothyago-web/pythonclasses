#ordem 
#if
#elif
#else


nome = input("Digite o seu nome: ")
idade = int(input("Digite o seu nome: "))
doenca_infec = (input("Suspeita de doença infect? ")).upper()

if idade >= 65: 
    print("O paciente", nome, "POSSUI atendimento prioritário" )

elif doenca_infec == "SIM":
    print("Deve ter uma sala reservada para ele")

else:
    print("O paciente", nome, "NÃO POSSUI atendimento prioritário e pode ir pra qualquer sala")
print("Fim")
