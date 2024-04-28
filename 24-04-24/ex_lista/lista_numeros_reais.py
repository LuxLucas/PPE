def get_numero():
    try:
        numero = float(input('Número: '))
        return numero
    
    except (TypeError, ValueError):
        print('\033[FErro: Número Inválido')
        return None
    

def inverter_numeros_lista(lista_com_numeros):
    lista_reversa = []
    for numero in lista_com_numeros[::-1]:
        lista_reversa.append(numero)
    return lista_reversa


lista_numeros = []
while len(lista_numeros) < 3:
    numero = get_numero()
    if not numero is None:
        lista_numeros.append(numero)
lista_numeros_reversa = inverter_numeros_lista(lista_numeros)
print(f'Lista numérica reversa: {lista_numeros_reversa}')