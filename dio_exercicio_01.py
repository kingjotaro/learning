def input_value(message):
    while True:
        try:
            valor = float(input(message))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

def deposit(balance, history):
    valor = input_value("Informe o valor do depósito: ")
    balance += valor
    history += f"Crédito:".ljust(20 - len(f"R$ {valor:.2f}")) + f"R$ {valor:.2f}\n"
    print(f"Depositado R${valor:.2f}\nSaldo total R${balance:.2f}\n")
    return balance, history

def withdraw(balance, limit, history, num_withdrawals, MAX_WITHDRAWALS):
    valor = input_value("Informe o valor do saque: ")
    if num_withdrawals >= MAX_WITHDRAWALS:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > balance:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limit:
        print("Operação falhou! O valor do saque excede o limite.")
    else:
        balance -= valor
        history += f"Débito:".ljust(20 - len(f"R$ {valor:.2f}")) + f"R$ {valor:.2f}\n"
        num_withdrawals += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!\nSaldo restando R${balance:.2f}\n")
    return balance, history, num_withdrawals

def show_history(balance, history):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not history else history)
    print(f"\nSaldo: R$ {balance:.2f}")
    print("==========================================")

def main():
    balance = 0
    limit = 500
    history = ""
    num_withdrawals = 0
    MAX_WITHDRAWALS = 3

    while True:
        print("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
        """)

        option = input("Escolha uma opção: ")

        if not option.isdigit():
            print("Por favor, insira um número válido.")
            continue

        option = int(option)

        if option == 1:
            balance, history = deposit(balance, history)
        elif option == 2:
            balance, history, num_withdrawals = withdraw(balance, limit, history, num_withdrawals, MAX_WITHDRAWALS)
        elif option == 3:
            show_history(balance, history)
        elif option == 4:
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
