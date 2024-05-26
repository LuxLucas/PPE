priNumero = float(input('Seu primeiro numero:'))
segNumero = float(input('Seu segundo numero:'))
if segNumero == 0:
    print('CÁLCULO IMPOSSÍVEL')
else:
    print('{:.2f}'.format(priNumero/segNumero))