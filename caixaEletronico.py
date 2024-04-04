class CaixaEletronico:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso. Saldo restante: R${self.saldo}"
        else:
            return "Saldo insuficiente para realizar o saque."

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}"
        else:
            return "Valor de depósito inválido."


def main():
    conta = CaixaEletronico()

    while True:
        print("\n1 - Consultar Saldo")
        print("2 - Sacar Dinheiro")
        print("3 - Depositar Dinheiro")
        print("0 - Quero sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f"Saldo atual: R${conta.consultar_saldo()}")

        elif escolha == "2":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            print(conta.sacar(valor_saque))

        elif escolha == "3":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            print(conta.depositar(valor_deposito))

        elif escolha == "0":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
