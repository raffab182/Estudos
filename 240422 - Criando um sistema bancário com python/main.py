menu = """
OPERAÇÕES:

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

while True:
  opcao = input(menu).lower()
  if opcao == "d":
    print("\nDeposito")
    valor = float(input("Informe o valor do depósito: ").replace(',', '.'))
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      print(f"\nDepósito de R$ {saldo:.2f} realizado com sucesso!")
      print("=========================================")
      print(f"\n*** Saldo atual: R$ {saldo:.2f} ***")
      print("=========================================")
    else:
      print("O valor informado é inválido.")

  elif opcao == "s":
    print("\nSaque")
    if numero_saques >= LIMITE_SAQUES:
      print("\nLimite de Saques diarios atingido.")
    else:
      valor = float(input("Informe o valor do saque: ").replace(',', '.'))
      if valor <= limite:
        if valor <= saldo:
          saldo -= valor
          numero_saques += 1
          extrato += f"Saque: R$ {valor:.2f}\n"
          print(f"\nSaque de R$ {saldo:.2f} realizado com sucesso!")
          print("=========================================")
          print(f"\n*** Saldo atual: R$ {saldo:.2f} ***")
          print("=========================================")
        else:
          print("\nSaldo Insuficiente.")
      else:
        print("\nValor é maior que o limite permitido.")
  elif opcao == "e":
    print("\n================ EXTRATO ================")
    if extrato == "":
      print("\nNão foram realizadas movimentações.")
      print("=========================================")
    else:
      print(extrato)
      print(f"\n*** Saldo atual: R$ {saldo:.2f} ***")
      print("=========================================")

  elif opcao == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")

    