class Conta:
    def __init__(self, numero, titular, saldo, limite): # função construtora
        print('Construindo objeto ...{}'.format(self))
        self.numero = numero
        self.titulo = titular
        self.saldo = saldo
        self.limite = limite


        # obs: self é a referência que sabe encontar aquele objeto que está sendo criado no módulo.

