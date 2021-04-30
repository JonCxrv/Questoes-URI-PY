while True:
    a, b = input().split(' ')
    a = int(a)
    b = int(b)

    if a == 0 and b == 0:
        break
    else:
        lista1 = []
        for s in range(a):
            lista1.append(str(input()))
        cc, d = input().split(' ')
        cc = int(cc)
        d = int(d)
        lista2 = []
        r = ''
        z = int(cc/a)
        for l in range(a):
            for c in range(b):
                r=str(r) + (int(d/b)*lista1[l][c])
            for k in range(z):
                lista2.append(r)
            r = ''
        for l in range(int(cc)):
            print(lista2[l])
        print()