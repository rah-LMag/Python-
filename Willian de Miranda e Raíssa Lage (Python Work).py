
# 1° Programa Caixa Eletrônico (match case [if, print, input])

("""
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
""")


# 2° Programa Joguinho: adivinhe o Nº (random.randint e while [if, else, print, input, and])

'''
import random 

random = random.randint (1, 15)
tentativa = 10

print ('Você tem ' , tentativa , 'tentativas para acertar um número aleatório gerado')
numero = int(input('Digite um número '))

while numero != random and tentativa > 0: 
    tentativa = tentativa - 1
    if numero > random:
        print ('Número incorreto. O número gerado aleatoriamente é menor.')
    else: 
        print ('Número incorreto. O número gerado aleatoriamente é maior.')
    print ('Você tem apenas mais ' , tentativa , 'tentativas para acertar.')
    numero = int(input('Tente novamente '))

if random == numero:
    print ('Você é um gênio!')
else: 
    print ('Seu número de tentativas acabou e você não conseguiu acertar.')
    print ('O número gerado era: ' , random)
'''


# 3° Programa calculadora de Fatorial (for [print, input])
("""
numero = int(input('Digite um número '))
fatorial = 1 
for c in range(1,numero+1):
    fatorial *= c 
print('O fatorial de ' , numero , ' é igual a ' , fatorial)
""")


# 4º Programa calculadora IMC (if, elif [print, input])

("""
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite seu altura: (m) '))
imc = peso / (altura**2)
print('O seu IMC é: ' , imc)

if imc < 18.5: 
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
	print('Você está no PESO NORMAL')
elif 25 <= imc < 30: 
     print('Você está ACIMA DO PESO normal')
elif 30 <= imc < 40:
   print('Você está em OBESIDADE ')
elif imc >= 40:
   print('Você está em OBESIDADE MÓRBIDA')
""")

# 5º Programa Calculador básico de prisão por homicídio (vetor, or, if, elif, else)

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