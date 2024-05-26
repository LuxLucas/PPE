Genero = input('Qual seu gênero (F || M) ?').upper()
match Genero:
    case 'F':
        print('F - Feminino')
    case 'M':
        print(f'M - Masculino')
    case _:
        print('Gênero inválido')