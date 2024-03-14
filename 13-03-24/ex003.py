#   Calculando custos de compra e entrega de uma biblioteca
QuantidadeDeCapas = int(input('Quantas capas deseja comprar ?: '))
ValorTotalDeCapas = (QuantidadeDeCapas * 24.95) - ((QuantidadeDeCapas * 24.95) * 0.35)

ValorTotalFrete = ((QuantidadeDeCapas - 1) * 0.75) + 3

ValorTotal = ValorTotalFrete + ValorTotalDeCapas
print(f'\n{"RESULTADO":=^50}')
print(f'Valor total das CAPAS R$: {ValorTotalDeCapas:,.2f}')
print(f'Valor total do FRETE R$: {ValorTotalFrete:,.2f}')
print(f'CUSTO TOTAL será de R$: {ValorTotal:,.2f}')