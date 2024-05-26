#   Juros Composto: Montante
ValorInicial = float(input('Valor inicial de investimento: '))
RentabilidadeMensal = float(input('Rentabilidade Mensal (em %): '))
TempoInvestimento = float(input('Tempo de investimento mensal: '))

Montante = ValorInicial * ((1 + RentabilidadeMensal/100) ** TempoInvestimento)

print(f'Seu montante final: R$ {Montante:,.2f}')
