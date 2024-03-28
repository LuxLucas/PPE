Nome = input('Nome: ').upper()
QuantidadeImoveis = int(input('Qtd imóveis vendidos: '))
TotalVenda = float(input('Valor total de vendas: R$ '))
Salario = 1500 + ((QuantidadeImoveis * 200) + (TotalVenda * 0.05))

print(f'{"RESULTADO":=^60}')
print(f'Salário Atual: {Salario:,.2f}')