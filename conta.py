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

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.saca(valor)




# obs: self é a referência que sabe encontar aquele objeto que está sendo criado no módulo.
# __saldo deixa o atributo privado - encapsula o acesso ao atributo
# self pode acessar um atributo assim como um método
