class Conta:
    def __init__(self, titular, numero):
        self.saldo = 2500.50
        self._numero = numero
        self._titular = titular

    pass

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ficar negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if valor >= 0:
            self.saldo -= valor
            if self.saldo >= valor:
                print("Saque realizado com sucesso")
        else:
            self.saldo += valor

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Valor depositado com sucesso")
        else:
            self.saldo -= valor

    def extrato(self):
        print("Nome Do Cliente:", self._titular, "\nSaldo Atual Da Conta:%.2f" % self._saldo)
