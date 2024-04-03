turno = input('Qual seu turno ? (M: matutino || V: vespertino || N: noturno): ').upper()
match turno:
    case 'M':
        print('Bom Dia!')
    case 'V':
        print('Boa Tarde!')
    case 'N':
        print('Boa Noite!')
    case _:
        print('Valor Inválido!')
        