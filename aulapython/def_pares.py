def pares(lista):
    for num in lista:
        if num % 2 ==0:
            print(num)

p1 = pares([11,22,33,44])
assert(p1 == [22,44])
assert(pares == ([11,33,55]) == [])
assert(pares == ([11,33,50,60]) == [50,60])


#--------------------------------------------------------------------------------

def pares(lista):
    resposta = []
    for num in lista:
        if num % 2 == 0:
            print(num)
            resposta.append(num)
    return resposta

assert(pares([11,22,33,44]) == [22,44])
assert(pares([11,33,55]) == [])
assert(pares([11,33,50]) == [50,60])

#--------------------------------------------------------------------------------

def achei(lista,elemento):
    for num in lista:
        if elemento == num:
            return True 
    return False
        
assert(achei([11,22,33,44],33) == True)
assert(achei([11,22,33,44],50) == False)
assert(achei([44],44) == True)
assert(achei([],44) == False)


# segunda forma de fazer: 

def achei(lista,elemento):
    for num in lista:
        if num == elemento:
            print("achei")

assert(achei([11,22,33,44],33) == True)   #assertionError
assert(achei([11,22,33,44],50) == False)
assert(achei([44],44) == True)
assert(achei([],44) == False)

