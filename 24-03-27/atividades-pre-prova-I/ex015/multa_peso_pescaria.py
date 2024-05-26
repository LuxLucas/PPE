from os import system

def limpar_console():
    system('cls')

def main():
    limpar_console()
    MultaPorQuilo = 0
    while True:
        try:
            PesoTotalPeixe = float(input("Peso de Peixe (Kg): "))
            break
        except (ValueError, TypeError) as Erro:
            print(f'\nErro: {Erro}')

    PesoExcedente = PesoTotalPeixe - 50
    if PesoExcedente > 0:
        MultaPorQuilo = (PesoTotalPeixe - 50) * 4

    print(f'{"RESPOSTA":=^60}')
    print(f'Peso Exedente: R$ {PesoExcedente:,.2f}')
    print(f'Peso Exedente: R$ {MultaPorQuilo:,.2f}')

if __name__ == '__main__':
    main() 