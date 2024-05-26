from os import system

def limpar_console():
    system('cls')

def receber_salario_bruto():
    while True:
        try:
            SalarioPorHora = float(input('Salário por hora: '))
            HorasDeTrabalhoMensal = float(input('Horas de trabalho mensal: '))
            break

        except (ValueError, TypeError) as Erro:
            print(f'\n{"Erro: {Erro}":^60}')

    return SalarioPorHora * HorasDeTrabalhoMensal

def main():
    limpar_console()
    SalarioBruto = receber_salario_bruto()
    print(f'{"RESPOSTA":=^60}')
    print(f'Salário Bruto: {SalarioBruto:,.2f}')


if __name__ == '__main__':
    main()