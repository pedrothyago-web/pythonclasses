# ---------------------------------------------------------------------------------------------------------------------------

# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

# ---------------------------------------------------------------------------------------------------------------------------

grade1 = float(input("Grade for the first subject: "))
grade2 = float(input("Grade for the second subject: "))
grade3 = float(input("Grade for the third subject: "))

grades = grade1 + grade2 + grade3

if grades < 21: #media 7
    print("You are rejected.")

else: 
    print("You are approved.")

#não usei bool, mas a resposta é a mesma.