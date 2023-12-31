import os


class Main:
    pass



print("testando o projeto")

from cliente import Cliente
from conta import Conta

cliente = Cliente("Caio", "(81)97905-6770")
conta = Conta(cliente.get_nome(), 0)
dnv = 'sim' or 'Sim'
while dnv == 'sim' or dnv == 'Sim':

    banco = str(input("Deseja realizar deposito ou saque:"))
    if banco == 'deposito':
        conta.depositar(float(input("Valor do Deposito:")))
        conta.extrato()

    elif banco == 'saque':
        conta.saque(float(input("Valor do Saque:")))
        conta.extrato()
    else:
        conta.extrato()
    dnv = str(input("Deseja executar novamente:"))
    os.system('cls')
else:
    print("\t\t\t\t\t\t\t\t\t\t.:Operação encerrada!!!:.")
