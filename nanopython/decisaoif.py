def maior(lista):
   resposta = 0
   for e in lista:
       if e > resposta:
           resposta = e
   return resposta


lista  = ["banana","abacate","mamao"]
lista2 = [100,200,300]
maior1 = maior(lista2)
maior2 = maior([900,874])
qq_eh_isso  = maior([])+3 #uai...