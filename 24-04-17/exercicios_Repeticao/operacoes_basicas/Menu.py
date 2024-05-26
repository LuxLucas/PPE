from os import system

class Menu:
    def limparConsole(self):
        system('cls')
              

    def receberPrimeiroNumerosFloatSoma(self):
        while True:
            self.limparConsole()
            try:
                PrimeiroNumero = float(input('Número 1: '))
                return PrimeiroNumero
            except (TypeError, ValueError) as Erro:
                print(f'Erro: {Erro}')


    def receberSegundoNumerosFloatSoma(self):
        while True:
            self.limparConsole()
            try:
                SegundoNumero = float(input('Mais Número 2: '))
                return SegundoNumero
            except (TypeError, ValueError) as Erro:
                print(f'Erro: {Erro}')


    def receberPrimeiroNumerosFloatSubtrair(self):
            while True:
                self.limparConsole()
                try:
                    PrimeiroNumero = float(input('Número 1: '))
                    return PrimeiroNumero
                except (TypeError, ValueError) as Erro:
                    print(f'Erro: {Erro}')


    def receberSegundoNumerosFloatSubtrair(self):
        while True:
            self.limparConsole()
            try:
                SegundoNumero = float(input('Menos Número 2: '))
                return SegundoNumero
            except (TypeError, ValueError) as Erro:
                print(f'Erro: {Erro}')


    def receberMultiplicando(self):
        while True:
            self.limparConsole()
            try:
                Multiplicando = float(input('Multiplicando: '))
                return Multiplicando
            except (TypeError, ValueError) as Erro:
                print(f'Erro: {Erro}')


    def receberMultiplicador(self):
        while True:
            self.limparConsole()
            try:
                Multiplicador = float(input('Multiplicador: '))
                return Multiplicador
            except (TypeError, ValueError) as Erro:
                print(f'Erro: {Erro}')


    def receberDividendo(self):
        while True:
            self.limparConsole()
            try:
                Dividendo = float(input('Dividendo: '))
                return Dividendo
            except (TypeError, ValueError) as Erro:
                print(f'Erro: {Erro}')


    def receberDivisor(self):
        while True:
            self.limparConsole()
            try:
                Divisor = float(input('Divisor: '))
                return Divisor
            except (TypeError, ValueError, ZeroDivisionError) as Erro:
                print(f'Erro: {Erro}')


    def mostrarOperacoes(self):
        self.limparConsole()
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')
        return input('\nSeu comando: ')
          