def get_elemento():
    elemento = input('Valor para elemento:')
    return elemento


def misturar_listas(primeira_lista_original, segunda_lista_original):
    lista_resultante = []
    primeira_lista = [item for item in primeira_lista_original]
    segunda_lista = [item for item in segunda_lista_original]

    while len(primeira_lista) + len(segunda_lista) > 0:
        if len(primeira_lista) > 0:
            lista_resultante.append(primeira_lista.pop(0))

        if len(segunda_lista) > 0:
            lista_resultante.append(segunda_lista.pop(0))

    return lista_resultante

primeira_lista = []
segunda_lista = []

print(f'\n{" PRIMEIRA LISTA ":=^60}')
for elemento in range(5):
    primeira_lista.append(get_elemento())

print(f'\n{" SEGUNDA LISTA ":=^60}')
for elemento in range(5):
    segunda_lista.append(get_elemento())

terceira_lista = misturar_listas(primeira_lista, segunda_lista)
print(f'\nPrimeira Lista: {primeira_lista}')
print(f'Segunda Lista: {segunda_lista}')
print(f'\nLista Resultante: {terceira_lista}')