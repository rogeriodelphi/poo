class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0): # função construtora
        print('Construindo objeto ...{}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('O titular {} possui o saldo de R$ {} em sua conta de número {} '.format(self.titular, self.saldo, self.numero))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor




        # obs: self é a referência que sabe encontar aquele objeto que está sendo criado no módulo.

