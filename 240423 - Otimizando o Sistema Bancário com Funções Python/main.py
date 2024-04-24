menu = """
OPERAÇÕES:
[u] Criar Usúario
[u1] Listar Usúarios
[c] Criar Conta
[c1] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
contas = {}
ultima_conta = 1000

def deposito(valor):
  global saldo
  global extrato
  if valor > 0:
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    print("=========================================")
  else:
    print("O valor informado é inválido.")

def saque(valor):
  global saque
  global saldo
  global extrato
  global limite
  global numero_saques
  if valor <= limite:
    if valor <= saldo:
      saldo -= valor
      numero_saques += 1
      extrato += f"Saque: R$ {valor:.2f}\n"
      print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
      print("=========================================")
    else:
      print("\nSaldo Insuficiente.")
  else:
    print("\nValor é maior que o limite permitido.")

def extrato_movimentacao():
  global extrato
  global saldo
  print("\n================ EXTRATO ================")
  if extrato == "":
    print("\nNão foram realizadas movimentações.")
    print("=========================================")
  else:
    print(extrato)
    print(f"\n*** Saldo atual: R$ {saldo:.2f} ***")
    print("=========================================")
    
def criar_usuario():
  global usuarios
  nome = input("\nInforme o nome: ")
  data_nascimento = input("Informe a data de nascimento: ")
  cpf = input("Informe o CPF: ").replace('.', '').replace('-','').replace(',','')
  endereco = input("Informe o endereço: ")
  usuario = {"nome": nome, "cpf": cpf, "Data Nascimento": data_nascimento, "Endereço": endereco}
  if usuarios == {} or cpf not in usuarios:
    usuarios[cpf] = usuario
    print("\nUsuário criado com sucesso!")
    print("=========================================")
  else:
    print("\nUsuário já cadastrado.")

def criar_conta():
  global ultima_conta
  global contas
  global usuarios
  agencia = "0001"
  ultima_conta += 1
  usuario = input("Informe o cpf do titular: ").replace('.', '').replace('-','').replace(',','')
  if usuario in usuarios:
    tconta = {"agencia": agencia, "Conta": ultima_conta, "Usuario": usuario}
    contas[ultima_conta] = tconta
    print("\nConta criada com sucesso!")
    print("=========================================")
  else:
    print("\nUsuário não cadastrado.")
while True:
  opcao = input(menu).lower()
  if opcao == "u":
    criar_usuario()
  elif opcao == "u1":
    print(f"\n{usuarios}")
  elif opcao == "c":
    criar_conta()
  elif opcao == "c1":
    print(f"\n{contas}")
  elif opcao == "d":
    deposito(float(input("\nDEPOSITO\n\n   Informe o valor do depósito: ").replace(',', '.')))
  elif opcao == "s":
    saque(float(input("\nSAQUE\n\n   Informe o valor do saque: ").replace(',', '.')))
  elif opcao == "e":
    extrato_movimentacao()
  elif opcao == "q":
    break
    
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")

