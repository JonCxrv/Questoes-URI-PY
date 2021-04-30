while True:
    n_postes = int(input())
    if n_postes == 0:
        break
    x = input()
    x = x.split()

    aux = ''
    count = 0
    distancia = 0

    for i in range(n_postes):
        if x[i] == '0':
            distancia += 1
            aux = '0'
            x.append(x[i])
        if x[i] == '1':
            break

    for i in range(distancia, len(x)):
        if x[i] == '0' and aux == '0':
            count += 1
            x[i] = '1'
        aux = x[i]
    print(count)