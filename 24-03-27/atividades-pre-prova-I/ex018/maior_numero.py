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

    print(f'{"RESPOSTA":=^60}')
    print(f'Maior Número: {max(Numeros)}')

if __name__ == '__main__':
    main()