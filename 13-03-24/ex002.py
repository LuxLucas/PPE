#   Juros Composto: Valor Inicial
Montante = float(input('Montante desejado: '))
RentabilidadeMensal = float(input('Rentabilidade Mensal (em %): '))
TempoInvestimento = float(input('Tempo de investimento mensal: '))

ValorInicial = Montante / ((1 + RentabilidadeMensal)**TempoInvestimento)

print(f'Seu investimento inicial: R$ {ValorInicial:,.2f}')
