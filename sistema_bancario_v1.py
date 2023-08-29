#Desafio de Projeto:
#Criando um sistema bancario
"""

menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[q] Sair
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
  opcao = str(input(menu)).strip()

  if opcao == "1":
    valor = float(input('Por favor, informe o valor do deposito: R$'))

    if valor > 0:
      saldo += valor
      extrato += (f'Deposito: R${valor:.2f}\n')

    else:
      print('Erro! O valor depositado e invalido.')

  elif opcao == "2":
    valor = float(input('Por favor, informe o valor do saque: R$'))

    if valor >= limite:
      print('Erro! O valor de saque excede o limite.')

    elif numero_saques == limite_saques:
      print('Erro! Numero de saques diario excedido.')

    elif valor > saldo:
      print('Erro! O valor de saque excede o saldo atual da conta.')

    elif valor > 0:
      saldo -= valor
      extrato += (f'Saque:    R${valor:.2f}\n')
      numero_saques += 1

    else:
      print('Erro! O valor informado e invalido.')

  elif opcao == "3":
    print('=================EXTRATO=================')
    print('Nao foram realizadas movimentacoes' if not extrato else extrato)
    print(f'\nSaldo: R${saldo:.2f}')
    print("=========================================")

  elif opcao == "q":
    print('Tenha um bom dia.')
    break

  else:
    print('Opcao invalida, tente novamente.')
