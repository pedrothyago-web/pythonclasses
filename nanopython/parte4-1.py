# Ler a idade da pessoa e criar uma variável que indica se ela é maior de idade

age = int(input("How old are you?: "))

if age <= 17:
    print("\nYou are underage.")

else:
    print("\nYou are of legal age.")