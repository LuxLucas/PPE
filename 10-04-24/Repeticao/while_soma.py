#Incompleto

from os import system


def limpar_console():
    system('cls')


def validar_numero(numero):
    if (numero < 0)and(numero != -1):
        print(f'\nNúmero Inválido')
        input('Precione "ENTER" para prosseguir...')
        return None
    else:
        return numero


def receber_numero():
    try:
        numero = float(input('Digite seu número (-1: parar repetição): '))
        numero = validar_numero(numero)
        return numero
    except (ValueError, TypeError) as erro:
        print(f'Erro: {erro}')
        return None
    

def is_not_none(numero):
    return not numero is None


def somar_numero(soma, numero, quantidade_de_numero):
    if is_not_none(numero):
        if is_not_none(soma):
            soma = soma + numero
            return soma, quantidade_de_numero
        return numero, quantidade_de_numero


def calcular_media(soma, quantidade_de_numero):
    if is_not_none(soma):
        media = soma / quantidade_de_numero
        return media


def comparar_menor_numero(menor_numero_atual, numero):
    if is_not_none(numero):
        if numero < menor_numero_atual:
            return numero
        else:
            return menor_numero_atual
    

def comparar_maior_numero(maior_numero_atual, numero):
    if is_not_none(numero): 
        if numero > maior_numero_atual:
            return numero
        else:
            return maior_numero_atual
    

def avisar_resultado(soma, media, maior_numero, menor_numero):
    limpar_console()
    print(f'Soma: {soma}')
    print(f'Média: {media}')
    print(f'Maior Número: {maior_numero}')
    print(f'Menor Número: {menor_numero}')


soma = None
numero = None
media = None
repeticao = 0
numeros_somados = 0
maior_numero = None
menor_numero = None

while numero != -1:
    limpar_console()
    repeticao += 1
    print(repeticao)
    numero = receber_numero()
    if repeticao == 1:
        if numero != -1:
            soma, numeros_somados = somar_numero(soma, numero, numeros_somados)
            maior_numero = numero
            menor_numero = numero
            media = numero
    else:
        maior_numero = comparar_maior_numero(maior_numero, numero)
        menor_numero = comparar_menor_numero(menor_numero, numero)
        soma, numeros_somados = somar_numero(soma, numero, numeros_somados)

media = calcular_media(soma, numeros_somados)
avisar_resultado(soma, media, maior_numero, maior_numero)