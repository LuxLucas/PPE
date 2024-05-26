Tipo = input('Tipo de combustível (A - ÁLCOOL || G - GASOLINA): ').upper()
Litros = float(input('Litros de combustível: '))

match Tipo:
    case 'A':
        if Litros <= 20:
            Preco = (Litros * 4.98) - ((Litros * 4.98)*0.02)
        else:
            Preco = (Litros * 4.98) - ((Litros * 4.98)*0.05)
    case 'G':
        if Litros <= 20:
            Preco = (Litros * 5.57) - ((Litros * 5.57)*0.04)
        else:
            Preco = (Litros * 5.57) - ((Litros * 5.57)*0.06)
    case _:
        print('Valor INVÁLIDO')

print(f'{"RESULTADO":=^50}')
print(F'O preço será de R$: {Preco:,.2f}')