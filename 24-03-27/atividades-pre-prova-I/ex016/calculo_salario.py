from os import system
from class_desconto import Desconto

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

def receber_salario_liquido(Salario):
    defDesconto = Desconto()
    return Salario - (defDesconto.calcular_desconto_total() * Salario)

def main():
    limpar_console()
    DescontoSalario = Desconto()

    SalarioBruto = receber_salario_bruto()
    SalarioSiliquido = receber_salario_liquido(SalarioBruto)

    print(f'\n{"RESPOSTA":=^60}')

    print(f'Salário Bruto: {SalarioBruto:,.2f}')
    print(f'Desconto IR: {DescontoSalario.DescontoSalarialImpostoDeRenda * SalarioBruto:,.2f}')
    print(f'Desconto INSS: {DescontoSalario.DescontoSalarialINSS* SalarioBruto:,.2f}')
    print(f'Desconto Sindicato: {DescontoSalario.DescontoSalarialSindicato * SalarioBruto:,.2f}')
    print(f'Desconto Total: {SalarioBruto * DescontoSalario.calcular_desconto_total()}')
    print(f'Salário Líquido: {SalarioSiliquido:,.2f}\n')

if __name__ == '__main__':
    main()

        