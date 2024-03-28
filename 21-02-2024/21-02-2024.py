print(f'{"SOMANDO":=^50}\n')
while True:
    try:
        priNumero = float(input('Digite seu primeiro número:'))
        segNumero = float(input('Digite seu segundo número:'))
        break
    except ValueError as erro:
        print(f'\n{"CARACTERE INVÁLIDO":=^50}')
        print('Tipo de erro:',erro,'\n')
        #if not segNumero.isnumeric():
        #    while not segNumero.isnumeric():
                
                
soma = priNumero + segNumero
print(f'\n{"RESULTADO":=^50}')
print(soma)
