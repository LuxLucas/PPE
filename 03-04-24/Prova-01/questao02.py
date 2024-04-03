def receber_data_nascimento(dia, mes, ano):
    try:
        dia = int(input('Dia de nascmento: '))
        mes = int(input('Mês de nascimento: '))
        ano = int(input('Ano de nascimento: '))
        return dia, mes, ano
    except (TypeError, ValueError) as erro:
        print('Data Inválida')
        return None, None, None


dia = None
mes = None
ano = None

dia, mes, ano = receber_data_nascimento(dia, mes, ano)
if (ano != None):
    idade = 2024 - ano
    if idade >= 18:
        print('\nPode retirar sua carteira de motorista.')
    else:
        print('\nNão pode retirar sua carteira de motorista.')
