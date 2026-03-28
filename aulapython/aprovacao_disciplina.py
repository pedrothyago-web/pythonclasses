# ---------------------------------------------------------------------------------------------------------------------------

# Faça um programa que retorne verdadeiro ou falso sobre sua aprovação na disciplina, considerando a presença
#  (um numero de 0 a 100, indicando a porcentagem de presença) e a nota (de 0 a 10)

# ---------------------------------------------------------------------------------------------------------------------------
# modelo 1

attendance_rate = int(input("What is your attendance rate this semester? (0-100%): "))

grade = int(input("What is your grade? (0-10): "))

if (attendance_rate >= 75) and (grade >= 6):
    print("You are approved.")

elif (attendance_rate >= 75) and (grade >= 4 and grade <= 6):
    print("You are of recuperation.")

elif (attendance_rate <= 75):
    print("You have failed.")

else:
    print("You have failed.")

# # ------------------ modelo com (def)

def aprovation(attendance_rate, grade):

    if (attendance_rate >= 75) and (grade >= 6):
        print("You are approved.")

    elif (attendance_rate >= 75) and (grade >= 4 and grade <= 6):
        print("You are of recuperation.")

    elif (attendance_rate <= 75):
        print("You have failed.")

    else:
        print("You have failed.")


aprovation(75, 3) #failed
aprovation(64, 10) #failed
aprovation(75, 5) #recuperation 
aprovation(75, 10) #approved
aprovation(100, 3) #failed
