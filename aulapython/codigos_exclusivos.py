n = 75
if n >= 90:
    conceito = "A"
if n >= 70:
    conceito = "B"
if n >= 50:
    conceito = "C"
if n < 50:
    conceito = "D"


# aqui será executado o B, pois o B é true. No entanto, há uma segunda condição após o B, que também é true e tendo essa codificação "if", será eccutado no print ("Conceito C"). 

n = 75
if n >= 90:
    conceito = "A"
elif n >= 70:
    conceito = "B"
elif n >= 50:
    conceito = "C"
elif n < 50:
    conceito = "D"

# Tendo esse exemplo com o "elif", será executado até a primeira condição ser true, sendo true, o python não lê o restante do código. Sendo printado: ("Conceito B"). 
