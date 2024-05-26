def receber_kilometragem_inicial():
    try:
        kilometragem = float(input('Kilometragem inicial: '))
        return kilometragem
    except (TypeError, ValueError) as erro:
        print('Valor Inválido')
        return None


def receber_kilometragem_atual():
    try:
        kilometragem = float(input('Kilometragem atual: '))
        return kilometragem
    except (TypeError, ValueError) as erro:
        print('Valor Inválido')
        return None
    

def receber_dias_alugado():
    try:
        dias = float(input('Dias alugados: '))
        return dias
    except (TypeError, ValueError) as erro:
        print('Valor Inválido')
        return None
    

def calcular_pagamento(kilometragem, dias):
    pagamento = (dias * 160)+(kilometragem * 0.80)
    return pagamento


kilometragem_inicial = receber_kilometragem_inicial()
kilometragem_atual = receber_kilometragem_atual()
dias_alugado = receber_dias_alugado()

if (kilometragem_inicial is float) or (kilometragem_atual is float) or (dias_alugado is float):
    kilometragem_rodada = kilometragem_atual - kilometragem_inicial
    total_pagar = calcular_pagamento(kilometragem_rodada, dias_alugado)
    print(f'TOTAL A PAGAR: R${total_pagar:,.2f}')
