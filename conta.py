class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0): # função construtora
        print('Construindo objeto ...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('O titular {} possui o saldo de R$ {} em sua conta de número {} '.format(self.__titular, self.__saldo, self.__numero))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print('O valor de R$ {} ultrapassa o limite de R$ {}.'.format(valor, (self.saldo + self.limite)))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.saca(valor)
        print("Transferência efetuada.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}


# obs: self é a referência que sabe encontar aquele objeto que está sendo criado no módulo.
# __saldo deixa o atributo privado - encapsula o acesso ao atributo
# self pode acessar um atributo assim como um método
