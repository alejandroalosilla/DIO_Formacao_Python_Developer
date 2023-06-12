"""
Projeto:
Fomos contratados por um grande banco para desenvolver o
seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem Python. Para a
primeira versão do sistema devemos implementar apenas 3
operações: depósito, saque e extrato.
"""
from time import sleep

menu = '''
***Menu***
---------------------
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
---------------------
=> '''

saldo = 1000
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
li_dep = []
li_saq = []

while True:

    opcao = input(menu).strip()

    if opcao == '1':
        print('***Depósito***')
        print('---------------------')
        while True:
            valor_deposito = float(input('Valor do Depósito [0 para cancelar]: R$'))
            if valor_deposito < 0:
                print('Por favor, digite um valor maior do que 0.')
                sleep(3)
            elif valor_deposito == 0:
                print('Operação de depósito cancelada!')
                sleep(3)
                break
            else:
                print(f'Depósito de R${valor_deposito:.2f} concluído!')
                sleep(3)
                saldo += valor_deposito
                li_dep.append(valor_deposito)
                break
    elif opcao == '2':
        print('***Saque***')
        print('---------------------')
        while True:
            valor_saque = float(input('Valor do saque [0 para cancelar]: R$'))
            if valor_saque == 0:
                print('Operação de saque cancelada!')
                sleep(3)
                break
            elif valor_saque > 500:
                    print('O limite de saque é de R$500,00 reais. Tente novamente.')
                    sleep(3)
            elif valor_saque > saldo:
                    print('Saldo Insuficiente! Tente novamente!')
                    print(f'Saldo: R${saldo:.2f}')
                    sleep(3)
            elif numero_saques < 3:
                print(f'Saque de R${valor_saque:.2f} concluído!')
                sleep(3)
                saldo -= valor_saque
                numero_saques += 1
                li_saq.append(valor_saque)
                break
            else:
                print('O limite de saques foi atingido.')
                sleep(3)
                break
    elif opcao == '3':
        print('***Extrato***')
        print('---------------------')
        if len(li_dep) == 0 and len(li_saq) == 0:
            print('Não foram realizadas movimentações.')
        else:
        
            print('Depósitos realizados: ')
            for indice, item in enumerate(li_dep):
                print(f'{indice + 1}º ....... R${item:.2f}')
        
            print('\nSaques realizados: ')
            for indice, item in enumerate(li_saq):
                print(f'{indice + 1}º ....... R${item:.2f}')
        print(f'\nSaldo Total: R${saldo:.2f}')
        print('---------------------')
        sleep(3)
    elif opcao == '0':
        print('Saindo...')
        sleep(3)
        break
    else:
        print(f'Operação inválida, por favor, selecione novamente a operação desejada.')
        sleep(3)
print('Obrigado pela preferência! Até mais!')
