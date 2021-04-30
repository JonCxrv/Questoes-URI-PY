casosteste = int(input())

for testes in range(casosteste):
    num_instru = int(input())
    lista = []
    for intru in range(num_instru):
        p = input().upper()
        if p == 'LEFT':
            lista.append(-1)
        elif p == 'RIGHT':
            lista.append(+1)
        elif p.startswith('SAME AS'):
            i = int(p[7:]) - 1
            lista.append(lista[i])  
    resultado = int(sum(lista))
    print(resultado)
