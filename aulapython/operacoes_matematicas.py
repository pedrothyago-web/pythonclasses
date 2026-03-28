# ---------------------------------------------------------------------------------------------------------------------------

# Exercício: Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

# ---------------------------------------------------------------------------------------------------------------------------

number1 = input("Write a number: ")
number2 = input("Write a another number: ")
operation = str(input("Which mathematical operation do you want to use?(+, -, *, /): "))

if operation == "+":
    result = number1 + number1
    print("The result of the sum is: ", result)

elif operation == "-":
    result = number1 - number1
    print("The result of the subtraction is: ", result)

elif operation == "*":
    result = number1 * number1
    print("The result of the multiplication is: ", result)

elif operation == "/":
    result = number1 / number1
    print("The result of the division is: ", result)

else:
    print("This is not a mathematical operation.")


