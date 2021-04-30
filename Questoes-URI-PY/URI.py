while True:
    n_teste = int(input())
    if n_teste == 0:
        break
    soma_uil = 0
    soma_ri = 0
    soma_ing = 0
    for testes in range(n_teste):
        uil = 0
        ri = 0
        ing = 0
    
        uil, ri, ing = input().split()
        uil = int(uil)
        ri = int(ri)
        ing = int(ing)
        valormax = max(uil,max(ri,ing))
        if (uil & (uil - 1)) == 0:
            soma_uil += 1
            if uil == valormax: 
                soma_uil += 1
        if (ri & (ri - 1)) == 0:
            soma_ri += 1
            if ri == valormax:
                soma_ri += 1
        if (ing & (ing - 1)) == 0:
            soma_ing += 1
            if ing == valormax:
                soma_ing += 1
    if soma_uil > soma_ri and soma_uil > soma_ing:
        print('Uilton')
    elif soma_ri > soma_uil and soma_ri > soma_ing:
        print('Rita')
    elif soma_ing > soma_uil and soma_ing > soma_ri:
        print('Ingred')
    else:
        print('URI')
        