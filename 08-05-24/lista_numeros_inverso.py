def valida_numero(numero):
    return not numero is None


def obter_numero():
    try:
        numero = float(input('Número: '))
        if valida_numero(numero):
            return numero
        return None
    except (TypeError, ValueError) as erro:
        print(f'Erro: {erro}')
        return None
    
lista_numeros = []
quantidade_numeros = len(lista_numeros)
while quantidade_numeros < 3:
    numero = obter_numero()
    if valida_numero(numero):
        lista_numeros.append(numero)
        quantidade_numeros = len(lista_numeros)

numeros_reverse = [numero for numero in lista_numeros[::-1]]
print(f'\n{numeros_reverse}')
