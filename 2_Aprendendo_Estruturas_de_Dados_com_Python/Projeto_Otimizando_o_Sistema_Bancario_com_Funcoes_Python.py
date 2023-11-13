def criar_usuario():
    print('\n******* Criar Usuário *******')
    print('-----------------------------')
    nome = input('Qual o seu nome? ').strip().capitalize()
    data_nasc = input('Qual sua data de nascimento?[00/00/0000] ').strip()
    cpf = input('Qual o seu CPF?[00000000000] ').strip()
    endereco = input('Qual o seu endereço?[cidade/estado] ').strip()

    cpf_em_uso = False

    for dado in contas:
        for k, i in dado['Usuario'].items():
            if cpf == i:
                cpf_em_uso = True
                break

    if cpf_em_uso:
        print('\nJa existe um usuário cadastrado nessse CPF!')
        return None
    else:
        dados = {'Nome': nome, 'Nascimento': data_nasc, 'CPF': cpf, 'Endereco': endereco}
        print('\nUsuário cadastrado com sucesso!')
        return dados


def criar_conta_corrente():
    print('\n******* Criar Conta Corrente *******')
    print('------------------------------------')

    contas.append({'Conta': len(contas) + 1, 'Agência': '0001', 'Usuario': usuario})
    print('\nConta criada com sucesso!')


def listar_contas():
    print('\n******* Lista de Contas *******')
    print('-------------------------------')
    
    if len(contas) == 0:
        print('\nNão há nenhuma conta cadastrada!')
    else:
        for d in contas:
            for k, v in d.items():
                print(f'{k}: {v}')
            print('\n')


def sacar(*, valor, extrato, saldo, numero_de_saques, limite_de_saques):
    
    if valor > saldo:
        print('\nSaldo Insuficiente!')
    elif numero_de_saques >= limite_de_saques:
        print('\nLimite de Saque Excedido!')
    else:
        saldo -= valor
        numero_de_saques += 1
        extrato['Saques'].append(valor)
    return saldo, numero_de_saques


def depositar(valor, saldo, extrato, /):
    saldo += valor
    extrato['Depositos'].append(valor)
    return saldo


def mostrar_extrato(saldo, *, extrato):
    print('******* EXTRATO *******')
    print('-----------------------')

    if sum(extrato['Saques'] + extrato['Depositos']) == 0:
        print('Não houve movimentações!')
    
    else:
        print('Saques realizados:')

        for indice, v in enumerate(extrato['Saques'], start=1):
            print(f'{indice}º.......R${v:.2f}')

        print('\nDepositos realizados:')

        for indice, v in enumerate(extrato['Depositos'], start=1):
            print(f'{indice}º.......R${v:.2f}')

    print(f'\nSaldo total: R${saldo:.2f}')

contas = []
saldo = 1000
limite = 500
numero_de_saques = 0
limite_de_saques = 3
extrato = {'Saques': [], 'Depositos': []}


menu = '''
***Banco Medeiros***
--------------------
[1] Sacar
[2] Depositar
[3] Extrato
[4] Criar Usuário
[5] Listar Contas
[0] Sair
--------------------
=> '''

while True:
    opcao = input(menu).strip()

    if opcao == '1':
        print('******* SAQUE *******')
        print('---------------------')

        while True:
            try:
                valor = float(input('Valor [0 para cancelar]: R$'))
            except ValueError:
                print('\nPor favor, digite um valor correto!')
            else:
                if valor == 0:
                    print('\nOperação cancelada!')
                    break
                elif valor < 0:
                    print('\nPor favor digite um valor maior que zero!')
                else:
                    saldo, numero_de_saques = sacar(valor=valor, extrato=extrato, saldo=saldo, numero_de_saques=numero_de_saques, limite_de_saques=limite_de_saques)
                    break
        
    elif opcao == '2':
        print('******* DEPOSITO *******')
        print('------------------------')
        
        while True:
            try:
                valor = float(input('Valor: R$'))
            except ValueError:
                print('Por favor, digite um valor correto!')
            else:
                if valor == 0:
                    print('\nOperação Cancelada!')
                    break
                elif valor < 0:
                    print('\nPor favor, digite um valor maior do que zero!')
                else:
                    saldo = depositar(valor, saldo, extrato)
                    break
        
    elif opcao == '3':
        mostrar_extrato(saldo, extrato=extrato)
    
    elif opcao == '4':
        usuario = criar_usuario()
        if usuario != None:
            while True:
                tipo_conta = input('''
******* Tipo de Conta *******
-----------------------------
[1] Corrente
[2] Poupança
[0] Cancelar
-----------------------------
=> ''').strip()
                if tipo_conta not in ('1', '2', '0'):
                    print('\nPor favor, digite uma da opções disponíveis!')
                else:
                    break
                    
            if tipo_conta == '1':
                criar_conta_corrente()
            elif tipo_conta == '2':
                print('\nDesculpe! Estamos trabalhando nisso!')
            elif tipo_conta == '0':
                print('\nOperação Cancelada!')
    
    elif opcao == '5':
        listar_contas()
    
    elif opcao == '0':
        print('Volte sempre!')
        break
    
    else:
        print('Por favor! Digite uma das opções acima!')
