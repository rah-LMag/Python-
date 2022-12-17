# 1° Programa: Caixa Eletrônico (match case [if, print, input])

'''
senha = int(input('Digite sua Senha: '))
saldo = float(input('Digite seu Saldo: '))
nome = input('Digite seu nome: ')
print('Olá ' , nome , 'seja bem-vindo(a)!')
print(' 1- Sacar \n 2- Depositar \n 3- Pagar Boleto \n 4- Cancelar')
opcao = int(input('Você deseja...?' ))
match opcao:
    case 1:
        print ('Você selecionou a opção de saque.')
        saque = float(input('Qual valor você deseja sacar: ')) 
        print('Seu saldo atual é de: ' , saldo - saque) 
        if saque > saldo: 
            print("Saldo Insuficiente.")     
    case 2:
        print ('Você selecionou a opção de deposito.')
        cont = int(input('Digite o número da conta que deseja realizar o deposito: '))
        dep = int(input('Qual valor deseja depositar?: '))
        print('Seu saldo atual é de: ' , saldo - dep)
        if dep > saldo: 
            print("Saldo Insuficiente.")
    case 3:
        print ('Você selecionou a opção de pagar boleto.')
        codg = int(input('Digite o código do boleto' ))
        boleto = int(input('Digite o valor do boleto: '))
        pagm = int(input('Digite o valor que irá pagar: '))
        print ('Você pagará ' , boleto - pagm , ' a mais no próximo mês.')
        print ('Seu saldo atual é de: ' , saldo - pagm)
    case 4:
        print ('Você cancelou seu atendimento. \n Até a próxima!')
'''

# 2º Programa: Calculador básico de prisão por homicídio (vetor, or, [if, else, print, input])

'''
fichacrim = ['', '', '', '', '']
fichacrim [0] = input('Já matou alguém? ')
fichacrim [1] = int(input('Se sim, quantos? '))
fichacrim [2] = input('Já matou animais? ')
fichacrim [3] = int(input('Se sim, quantos? '))

if fichacrim [0] == 'sim' or fichacrim [2] == 'sim':
    print ('Você será preso e investigado por estes atos.')
    if fichacrim [1] > 2 or fichacrim [3] > 2:
        print ('O seu tempo de prisão será muito bem determinado!')
else:
    print ('Você está liberado por enquanto.')
'''

# 3º Programa: Jogo de adivinhação - Cores (while [random, vetor, if, elif, else, and, or, print, input])

'''
color = ['vermelho', 'azul', 'amarelo', 'verde', 'roxo', 'laranja', 'preto', 'branco', 'cinza', 'beje', 'marrom' ]
import random 
color3 = random.choice(color)
tent = 5

print ('Jogo da adivinhação: cores primárias e secundárias e neutras')
print ('As cores que poderão ser geradas são: \n  Vermelho, Azul, Amarelo, Verde, Roxo, Laranja, Preto, Branco, Cinza, Beje, Marrom')
print ('Você terá ' , tent , ' tentativas.')
print ('____________________________________________')

color4 = input('Qual é a cor? ')

while color4 != color3 and tent != 1:
    print ('Opa, não é esta cor.') 
    tent = tent -1
    print ('Você tem mais ' , tent , ' tentativa (s).')
    if color3 == color [0] or color3 == color [2] or color3 == color [5]:
        print ('A cor é quente.')
    elif color3 == color [1] or color3 == color [3] or color3 == color [4]:
        print ('A cor é fria.')
    else:
        print ('A cor é neutra. ')
    
           
    color4 = input('Tente novamente: ')

if color4 == color3:
    print ('Você é um gênio!')
else:
    print ('Suas tentativas acabaram e você não conseguiu adivinhar a cor. \n A cor gerada era: ' , color3)    
'''

# 4° Programa: Contador/ Regressivo (while, for, match case[if, elif, print, input])

'''
opcao = int(input(' 1 - Contagem de números (regressiva ou não) que estão dentre os dois pelo quais você solicitar. \n 2 - Ou Fibonacci dos primeiros valores do qual você solicitar? \n \n'))

match opcao:

    case 1:

        ni = int(input(' \n Qual o número que terá início? '))
        nf = int(input(' Qual o número será o fim? '))

        if ni < nf:
            for cont in range (ni,nf+1):
                print (cont)

        elif ni > nf:
            for cont in range (ni,nf,-1):
                print (cont)
            print (nf)

    case 2:
    
        print ('OBS: caso queira que seja exibidos a quantidadde de valores, digite 0 na segunda pergunta.')
        print ('Caso queira saber qual é o Fibonnacci de uma posição (em nº), digite 0 na primeira pergunta.')
        qnt = int(input(' \n Quantos valores você quer que seja exibido? '))
        num = int(input(' \n Digite a posição que deseja descobrir: '))
        n1 = 0
        n2 = 1
        q = 2
        if num == 0:
            print (n1 , '\n' , n2)
            while q < qnt: 
                n3 = n1 + n2
                print (n3)
                n1 = n2
                n2 = n3
                q += 1
        elif qnt == 0:
            for i in range (0,num):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
            print ('O Fibonacci da ' , num , 'º posição é: ' , n1)
'''
