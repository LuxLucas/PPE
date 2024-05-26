repeticao = 6

def validar_numero(numero):
    return type(numero) is int


def obter_numero():
    try:
        numero = int(input('Digite um número inteiro: '))
        return numero
    except (TypeError, ValueError) as erro:
        print(f'Erro: {erro}')
        return None


def criar_lista():
    lista = []
    numeros_na_lista = 0
    while numeros_na_lista < repeticao:
        numero = obter_numero()
        if validar_numero(numero):
            lista.append(numero)
            numeros_na_lista += 1
    return lista


def mesclar_listas(primeira_lista, segunda_lista):
    lista_mesclada = []
    for indice in range(repeticao):
        soma_elementos = primeira_lista[indice] + segunda_lista[indice]
        lista_mesclada.append(soma_elementos)
    return lista_mesclada


print(f'{" PRIMEIRA LISTA ":=^45}')
primeira_lista = criar_lista()

print(f'\n{" SEGUNDA LISTA ":=^45}')
segunda_lista = criar_lista()

print()
print(f'\n{" RESPOSTA ":=^45}')
lista_mesclada = mesclar_listas(primeira_lista, segunda_lista)
print(lista_mesclada)