tabuada = int(input("Digite um número para fazer a tabuada: "))
print("Tabuada do número ", tabuada)

for valor in range(1, 21, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str(tabuada * valor))