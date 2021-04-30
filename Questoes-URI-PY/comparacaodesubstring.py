while True:
    try:
        frase1 = input()
        frase2 = input()
        maior_sub = 0
        count = 0

        for i in range (len(frase1)):
            if i > len(frase2)-1:
                break

            for j in range(len(frase2)):
                if frase1[i] == frase2[j]:
                    x = i
                    for k in range(j, len(frase2)):
                        if x > len(frase1)-1:
                            break
                        if frase1[x] != frase2[k]:
                            break
                        count += 1
                        x += 1
                    if count > maior_sub:
                        maior_sub = count
                    count = 0        
                                
        print(maior_sub)
    except EOFError:
        break