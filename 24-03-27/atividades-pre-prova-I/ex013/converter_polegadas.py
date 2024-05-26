from os import system

def limpar_console():
    system('cls')

def converter_polegadas(polegadas):
    print((polegadas * 2,54) * 10)
    return (polegadas * 2,54) * 10

def main():
    while True:
        limpar_console()
        try:
            Polegadas = float(input('Polegadas: '))
            break
        except (ValueError, TypeError) as Erro:
            print(f'\n{"Erro: {Erro}":=^60}')

    PolegadaConvertida = type(Polegadas)
    print(f'{"RESPOSTA":=^60}')
    print(PolegadaConvertida)
    print(f'Milímetros: {PolegadaConvertida:.2f}')


if __name__ == '__main__':
    main()