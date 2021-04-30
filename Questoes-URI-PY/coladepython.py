'''ALGUMAS COLAS PORQUE AINDA TO APRENDENDO PYTHON.'''



#atalhos
#ALT + SETA 
#SHIFT + ALT + SETA COPIA CODE
# CTRL + ' TERMINAL

#coisas que podem ser uteis
#variavel.cout(oqeu quero contar)
#print(f'o valor mais alto é {max(lista)}')
#print(f'o valor mais baixo é {min(lista)}')
#lista.remove('valor que eu quero remover')
#del(lista[0]) apagar a primeira informação
#lista.append('variavel') para add algo a lista
#lista.insert(posição que eu quero ex:0,variavel) para add algo a posição que eu quero

#lista.sort() #organizar lista em forma crescente
#lista.sort(reverse = True) #organiza a lista em forma descrecente
#len(lista) = quantos elementos eu tenho na lista
#b = a ligação entre as listas // b = a[:] cria uma copia 


'''print('824', '176','070', sep='.',end='-')
print('18')
nome = 'luiz'
idade = 32
peso = 80.5
altura = 1.80
ano_atual= 2019
#imc = peso / altura

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"o IMC de {nome} e {peso/altura**2:.2f}.")
print(f"Luiz nasceu em {ano_atual - idade}.")'''


"""nome = input("qual seu nome?\n")
idade = int( input("qual usa idade?\n"))

#idade_min = 18

if 20 <= idade <= 30:
    print(f"{nome} pode pegar o emprestimo")
else:
    print(f"{nome} NAO pode pegar o emprestimo mals ai")"""


'''a = ''
b = 0
if not b:
    print('preecha o valor de A seu merda')'''


"""
#VERIFICAR SE EXISTE LETRA NO NOME INSERIDO.
n = input('qual a letra que deseja procurar?')
if n in nome:
    print('existe essa porra ai no teu nome.')
else:
    print('nao existe essa merda burro')
"""


#FUNÇÃO LEN. (QUANTIDADE DE CARACTERES)

#len(variavel que eu quero saber a quantidade de letras na palavra ou frase)
#teste = input('digite o teste: ')
#print(f'a quantidade de caracteres nesta palavra é {len(teste)}')

'''num_1 = a
num_2 = 3
try:    #tentar fazer isso
    print(num_1 + num_2)
except:     #se nao conseguir faça isso
   print('error')'''


'''#ignorando uma linha de codigo com 3 pontos
valor = True
if valor:
    ...
else:
    print("teste")'''


'''
#IMPAR OU PAR, SEM QUEBRAR AO DIGITAR LETRA GRAÇAS AI "ISDIGIT()"
n = input('informe o numero meu pit: ')

if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print('é par')
    else:
        print('é impar')
else:
    print('isso nao é um numero inteiro meu chapa') '''


'''hora = input('quer horas mano? ')

if hora.isdigit():
    hora = float(hora)
    if 0 <= hora <= 11:
        print('bom dia negao')
    elif 11 < hora <= 17:
        print('boa tarde negao')
    else:
        print('boa noite negao')
else:
    print('essa nao é ahora chapa')'''

#usando "LEN" para ver o tamanho da string


'''nome_us = input('teu nome bro? ')

if len(nome_us) <= 4:
    print('nome curto')
elif 4 < len(nome_us) < 6:
    print('seu nome é normal')
else:
    print('nome grandão vei')'''


'''#formantando valores em python
variavel = int(input())
print(f"{variavel:#^10.2f}")'''  # <--centralizando entre caracteres


'''#WHILE IM PYTHON
x = int(input())
while x < 10:
    if x == 2:
        x+=1
        continue    #POSSO USAR A FUNÇÃO '## BREAK ##' CASO QUEIRA PARAR AO INVES DE PULAR O NUMERO 2 NESTE CASO
    print(x)
    x+=1
'''


''' # COLOCANDO LETRAS INSERIDAS PELO USUARIO EM MAISCULA COM WHILE
frase = "jhonatan teste teste"
contador = 0
nova_string = ''
letra_maiscula = input("letra que deseja colocar em maiscula?")

while contador < len(frase):
    letra = frase [contador]

    if letra == letra_maiscula :
        nova_string += letra_maiscula.upper()
    else :
       nova_string += letra
    contador += 1
print(nova_string)'''


# WHILE
'''
sexo = input('digite o seu sexo [M/F]: ').strip().upper()[0] #strip tira espaco do inicio e fim da string // [0] pega somente o primiero valor digitado 
while sexo not in 'MF':
    sexo = input('invalido - informe m ou f').strip().upper()[0] 
print(f"o sexo {sexo} foi registrado com sucess")'''

#JOGO DE ADIVINHAÇÃO TOP SHOW
'''
from random import randint
computador = randint(0,10)
print('sou seu pc... pensei num numero aqui entre 0 e 10 quel é ele?')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual tu acha que é ? '))
    palpites +=1 
    if (player > 10) or (player < 0):
        print('o numero escolhido foi entre 0 e 10 burro. ')
    else:
        if player == computador:
            acertou = True
            break
        else :
            if player < computador:
                print ('quase... porem o numero que foi sorteado é mais alto do que isso')
            else:
                print('quase... porem o numero que foi sorteado é mais baixo que isso')
print(f'voce ACERTOU e precisou de {palpites} palpites para isso') '''



#WHILE INFINITO USANDO BREAK
'''c = 0
while True:
    stop = int(input('digite um valor (999 para parar): '))
    if stop == 999:
        break
    else:
        c += stop
print(f'soma dos valores igual a: {c}')
'''

#FOR

#atividada de numeros impares divisiveis por 3
'''
soma = 0
cont = 0
for c in range (1,500,2):
    if c % 3 == 0:
        cont +=1
        soma += c
print(f'a soma de todos os {cont} é {soma}')'''

#tabuada com for
'''t = int(input('digite o numero que deseja saber a tabuada: '))  
for c in range(0, 11):
    m = t*c
    print(f'{t} X {c} = {m}')'''


#PALINDROMO
'''frase = input('digite um frase: ').strip().upper()
separadas = frase.split()                            #neste linha separei as palavras num vetor pelos espaços entre elas
junto = ''.join(separadas)                           #nesta linha juntei tudo ou seja nessas duas linhas removi os espaçoes de uma frase
inverso = ''  #se eu nao usar o FOR posso fazer só inverso = junto[::-1]
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto,inverso)
if inverso == junto:
    print('é palindromo')
else:
    print('nao é palindromo')'''
    
    



#OUTRO EXEMPLO DE FOR
'''n = int(input('insira a quantidade de pessoas: '))
idadegeral = 0
for p in range(1, n+1):
    print(f'----- {p}(a) pessoa ------') 
    nome = input('nome: ') 
    idade = int(input('idade: '))
    Sexo = input('sexo m ou f pf: ')
    idadegeral += idade    
print(f'a media de idade das pessoas é {idadegeral/2}')'''


