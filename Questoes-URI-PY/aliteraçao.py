while True:
    try:
        frase = input()
        qnt_alit = 0
        frasesplit = frase.split()
        armazenar = []
        for p in frasesplit:
            armazenar.append(p[0].upper())
        i = 0
        armazenar.append('')
        for alit in armazenar[1:len(armazenar)]:
            if armazenar[i] == alit and armazenar[i+2] != alit:
                qnt_alit += 1
            i += 1
        print(qnt_alit)
    except EOFError:
        break