maior_plvr = ''
while True:   
    frase = input()
    frasesplit = frase.split()

    if frasesplit[0] == '0':
        break
    else:
        for qnt in range(len(frasesplit)):
            exibir_qnt = len(frasesplit[qnt])
            if qnt == 0:
                print(exibir_qnt,end='')
            else:
                print('-', end='')
                print(exibir_qnt,end='')
        print()
        for maior in frasesplit:
            if(len(maior_plvr) <= len(maior)):
                maior_plvr = maior
print()
print(f'The biggest word: {maior_plvr}')