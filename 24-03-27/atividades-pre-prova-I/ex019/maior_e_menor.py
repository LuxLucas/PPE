from os import system

def limpar_console():
    system('cls')

def main():
    limpar_console()
    Numeros = []
    try:
        for indice in range(3):
            Numeros.append(float(input(f'Número {indice+1}: ')))
    except (TypeError, ValueError) as Erro:
        print(f'\nErro: {Erro}')

    MaiorNumero = max(Numeros)
    Numeros.remove(MaiorNumero)
    MenorNumero = min(Numeros)
    Numeros.remove(MenorNumero)
    MedioNumero = Numeros[0]
    
    print(f'{"RESPOSTA":=^60}')
    print(f'Maior Número: {MaiorNumero}')
    print(f'Médio Número: {MedioNumero}')
    print(f'Menor Número: {MenorNumero}')


if __name__ == '__main__':
    main()