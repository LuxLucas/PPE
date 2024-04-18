from Menu import Menu

Painel = Menu()


def mostrarResposta(Operacao, Resposta):
     Painel.limparConsole()
     print(f'RESPOSTA DA {Operacao}: {Resposta}')
     input('Pressione "ENTER" para continuar...')


def somar():
    PrimeiroNumero = Painel.receberPrimeiroNumerosFloatSoma()
    SegundoNumero = Painel.receberSegundoNumerosFloatSoma()
    ResultadoSoma = PrimeiroNumero + SegundoNumero
    mostrarResposta('SOMA', ResultadoSoma)


def subtrair():
    PrimeiroNumero = Painel.receberPrimeiroNumerosFloatSubtrair()
    SegundoNumero = Painel.receberSegundoNumerosFloatSubtrair()
    ResultadoSubtracao = PrimeiroNumero - SegundoNumero
    mostrarResposta('SUBTRAÇÃO', ResultadoSubtracao)


def multiplicar():
    Multiplicando = Painel.receberMultiplicando()
    Multiplicador = Painel.receberMultiplicador()
    ResultadoMultiplicacao = Multiplicando * Multiplicador
    mostrarResposta('MULTIPLICAÇÃO', ResultadoMultiplicacao)


def dividir():
    Dividendo = Painel.receberDividendo()
    Divisor = Painel.receberDivisor()
    if Divisor != 0:
        ResultadoDivisao = Dividendo / Divisor
    else:
        ResultadoDivisao = 'Divisor não pode ser 0 (Zero)'
    mostrarResposta('DIVISÃO', ResultadoDivisao)


def realizarOperacao(Comando):
    match Comando:
            case '1': somar()
            case '2': subtrair()
            case '3': multiplicar()
            case '4': dividir()
         


def main():
    while True:
        Comando = Painel.mostrarOperacoes()
        if Comando == '5':
            break
        realizarOperacao(Comando)


if __name__ == "__main__":
    main()