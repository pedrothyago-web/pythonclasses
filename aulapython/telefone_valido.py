# len(s) diz o tamanho da string 

def tel_valido(string):
    tamanho = len(string)
    if tamanho < 8:
        return False
    elif tamanho >= 11: 
        return False 
    else: 
        return True 


assert(tel_valido("123") == False)
assert(tel_valido("1133334444") == True)
assert(tel_valido("34444") == False)
assert(tel_valido("15989893322") == True)
assert(tel_valido("989893322") == True)

#------------------------------------------------------------
# Exercise - Média

def altura_valida(a): 
    if a < 0.5 or a > 2.8:
        return False
    return True 
    
def media(p1,p2,p3):
    if altura_valida(p1) and altura_valida(p2) and altura_valida(p3):
        return  (p1,p2,p3) / 3
    return False

     

assert(media(2,2,2) == 2)
assert(media(1.9,2,2.1) == 2)
assert(1.59 <= media(1.5,1.7,1.6) <= 1.61)
assert(media(3,2,2.1) == False)
