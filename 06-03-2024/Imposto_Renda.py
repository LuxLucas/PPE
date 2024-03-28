def Verificar_Imposto(Imposto):
    if Imposto <= 0:
        return 0
    else:
        return Imposto

def Calcular_Imposto(Salario):
    if Salario <= BaseCalculo[0]:
        return Salario
    
    elif Salario <= BaseCalculo[1]:
        Imposto = (Salario * TaxaAliquota[0]) - DeducaoTabelada[0]
        return Verificar_Imposto(Imposto)
    
    elif Salario <= BaseCalculo[2]:
        Imposto = (Salario * TaxaAliquota[1]) - DeducaoTabelada[1]
        return Verificar_Imposto(Imposto)
    
    elif Salario <= BaseCalculo[3]:
        Imposto = (Salario * TaxaAliquota[2]) - DeducaoTabelada[2]
        return Verificar_Imposto(Imposto)
    
    else:
        Imposto = (Salario * TaxaAliquota[3]) - DeducaoTabelada[3]
        return Verificar_Imposto(Imposto)
        

ImpostoRenda = None
BaseCalculo = [2259.2, 2826.65, 3751.05, 4664.68]
TaxaAliquota = [0.075, 0.15, 0.225, 0.275]
DeducaoTabelada = [169.44, 381.44, 662.77, 896]
DeducaoDependente = 189.59

print(f'{"IMPOSTO DE RENDA":=^60}')

TipoIR = int(input('Tipo de IR desejado ? (Tradicional:1/Simples:2)'))
if TipoIR == 1:
    print(f'\n{"IMPOSTO DE RENDA TRADICIONAL":=^60}')

    Salario = float(input('Seu salário: '))
    INSS = float(input('Seu INSS: '))
    Dependentes = int(input('Quantidade de dependentes: '))

    SalarioBase = Salario - (INSS + (Dependentes * DeducaoDependente))

else:
    DeducaoSimples = 2259.2 * 0.25
    print(f'\n{"IMPOSTO DE RENDA SIMPLIFICADO":=^60}')
    Salario = float(input('Seu salário: '))

    SalarioBase =  Salario - DeducaoSimples
    
ImpostoRenda = Calcular_Imposto(SalarioBase)

print(f'\n{"RESULTADO":=^60}')
print(f'Seu IR é de: R$ {ImpostoRenda:.2f}')
