ncasos = int(input())

for i in range(ncasos):
    n, k = input().split()
    n = int(n)
    k = int(k)
    if n == 1:
        resultado = 1
    else:
        resultado = ((n-1 + k + k - 1) % n + 1)
    print('Case {}: {}'.format(i,resultado))