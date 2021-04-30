#Nem eu entendo como saiu isso, meio que so aceita.
while True:
    try:    
        C, N = input().split()
        C = int(C)
        N = int(N)
        chav_1 = input()
        chave_2 = input() 
    
        for i in range(N):
            fraseEncript = input()
            a = fraseEncript

            for ic in range(0,C):
                if chave_2[ic].isalnum() == True:
                    if chave_2[ic].isnumeric() == False:
                        a = a.replace(chave_2[ic], chav_1[ic])
                        a = a.replace(chave_2[ic].lower(), chav_1[ic].lower())
                    else:
                        a = a.replace(chave_2[ic].lower(), chav_1[ic].lower())    
                else:
                    a = a.replace(chave_2[ic].lower(), chav_1[ic].lower())

            for ic in range(C):
                for ik, c in enumerate(a):
                    if c == fraseEncript[ik] and c.upper() == chav_1[ic]:
                        if chave_2[ic].isnumeric() == False:
                            if c != chav_1[ic]:
                                b = a[ik:]    
                                b = b.replace(chav_1[ic].lower(), chave_2[ic].lower(), 1) 
                                c = a[:ik] + b
                                a = c
                            else:
                                b = a[ik:]    
                                b = b.replace(chav_1[ic].upper(), chave_2[ic].upper(), 1) 
                                c = a[:ik] + b
                                a = c
                        else:
                            b = a[ik:]    
                            b = b.replace(chav_1[ic].lower(), chave_2[ic].lower(), 1) 
                            c = a[:ik] + b
                            a = c                
            print(a)
        print()
    except EOFError:
        break
