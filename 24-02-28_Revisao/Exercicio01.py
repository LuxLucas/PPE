print(f'\n{"JUROS COMPOSTOS":=^50}')
while True:
    try:
        Capital = float(input('Digite seu capital inicial: '))
        Rentabilidade = float(input('Digite a rentabilidade ANUAL prevista (%): '))
        MesesAplicado = float(input('Quantos meses será aplicado: '))
        Montante = Capital * (1 + ((Rentabilidade/100)/12)) ** (MesesAplicado)
        break
    except (TypeError, ValueError) as erro: 
        print(f'ERRO: {erro}')
print(f'\nSeu montante será de: {Montante:.2f}\n')
print(f'{"FIM":=^50}')
