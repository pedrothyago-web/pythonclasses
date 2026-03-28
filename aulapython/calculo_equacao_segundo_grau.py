# ---------------------------------------------------------------------------------------------------------------------------

# Escreva um programa que calcule as raízes de uma equação de segundo grau: ax**2 + bx + c == 0

# ---------------------------------------------------------------------------------------------------------------------------

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

print(" ")
print(f"Delta = {delta}")
print(" ")

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raizes são:\n {x1:.2f} e {x2:.2f}")

elif delta == 0:
    x = -b / (2*a)
    print(f"A raiz é: {x}")

else:
    print("Não há raizes porque o delta é negativo.")

