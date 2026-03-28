# Ler duas palavras, e criar uma variável palavras_em_ordem, que é True se elas foram dadas na ordem alfabética, e False caso contrário
# Se elas forem iguais, então diremos que elas estão em ordem alfabética
# sorted(frases)


word1 = input("Wrote a word: ")
word2 = input("Wrote a another word: ")

words = [word1, word2]

words_in_order = sorted(words)

print(words_in_order)