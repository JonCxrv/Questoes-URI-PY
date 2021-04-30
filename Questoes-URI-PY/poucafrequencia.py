T = int(input())
for teste in range(T):
    num_alunos = int(input())
    nome_alunos = input().split()
    freq_aluno = input().split()
    resultado = []
    for i in range(len(nome_alunos)):
        M_count = 0
        A_count = 0
        P_count = 0

        C = list(freq_aluno[i])
        for j in C:
            if j == "P":
                P_count += 1
            elif j == "A":
                A_count += 1
            elif j == "M":
                P_count += 0

        total = A_count + P_count
        if total != 0:
            if P_count / total < 0.75:
                resultado.append(nome_alunos[i])
        else:
            pass

    print(*resultado)