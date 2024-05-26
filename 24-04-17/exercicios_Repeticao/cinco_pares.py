from os import system

def limparConsole():
    system('cls')


def receberNumeroPositivo():
    while True:
        try:
            Numero = int(input('Digite um número inteiro: '))
            if Numero > 0:
                return Numero
            else:
                print('Numero Negativo')
        except (TypeError, ValueError) as Erro:
            print(f'Erro: {Erro}')


def isPar(Numero):
    return Numero % 2 == 0


def mostrarNumerosPares(ListaComPares):
    if len(ListaComPares) == 0:
        print('Lista Vazia')
    else:
        for Indice in range(len(ListaComPares)):
            print(ListaComPares[Indice])



def main():
    NumerosParesDigitados = []
    for Contador in range(5):
        limparConsole()
        print(f'Números Recebidos: {Contador}')
        NumeroDigitado = receberNumeroPositivo()
        if isPar(NumeroDigitado):
            NumerosParesDigitados.append(NumeroDigitado)
            
    limparConsole()
    print(f'{"RESULTADO":=^60}')
    mostrarNumerosPares(NumerosParesDigitados)
    print(f'{"=":=^65}')


if __name__ == "__main__":
    main()