from os import system


def limpar_console():
    system('cls')


def receber_tabuada():
    try:
        numero_tabuada = int(input('Digite sua tabuada: '))
        return numero_tabuada
    except (TypeError, ValueError) as erro:
        print('\nNúmero Inválido')
        input('Digite "ENTER" para prosseguir...')


def criar_tabuada(numero_tabuada):
    for incremento in range(1, 11):
        print(f'{numero_tabuada} X {incremento} = {numero_tabuada*incremento}')


def main():
    limpar_console()
    tabuada = receber_tabuada()
    print(f'{f"Tabuada de {tabuada}":=^50}')
    criar_tabuada(tabuada)
    print(f'{"FIM":=^50}')


if __name__ == '__main__':
    main()