frase = input()
frasesplit = frase.split()
saida = ''
for i in frasesplit:
    for j in range (1,len(i),2):
        saida = saida + i[j]
    saida = saida + ' '
#s = saida[0:-1:1] 
print(saida)