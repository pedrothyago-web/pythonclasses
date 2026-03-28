#for

#range(ínicio, fim, passo)

for contador in range(1, 4,):
    nota_1 = float(input("Digite a 1° nota: "))
    nota_2 = float(input("Digite a 2° nota: "))

    print(f"Média: {(nota_1+nota_2)/2}")

for i in range(1,6):
    if i == 4:
        continue
    print(i)

for i in range(1,6):
    if i == 4:
        break
    print(i)