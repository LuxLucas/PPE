def validar_nota(nota):
    return nota > 0 and nota < 10


def obter_nota():
    try:
        nota = float(input('Nota: '))
        if validar_nota(nota):
            return nota
        else:
            return None
    except (ValueError, TypeError) as erro:
        print('ERRO:', erro)
    

def media_notas(lista_com_notas):
    soma_notas = sum(lista_com_notas)
    tamanho_lista = len(lista_com_notas)
    media = soma_notas / tamanho_lista
    return media


def mostrar_notas(lista_com_notas):
    print(f'Maior nota: {max(lista_com_notas)}')
    print(f'Menor nota: {min(lista_com_notas)}')
    print(f'Média notas: {media_notas(lista_com_notas)}')

    lista_com_notas_crescente = [nota for nota in sorted(lista_com_notas)]
    print(f'\nNotas crescentes: {lista_com_notas_crescente}')

    lista_com_notas_decrescente = [nota for nota in sorted(lista_com_notas, reverse=True)] # Ou lista.reverse()
    print(f'Notas decrescentes: {lista_com_notas_decrescente}')


def main():
    lista_notas = []
    while len(lista_notas) <= 2:
        nota = obter_nota()
        if not nota is None:
            lista_notas.append(nota)
    print(f'\n{"RESULTADO":=^60}')
    mostrar_notas(lista_notas)
    

if __name__ == '__main__':
    main()