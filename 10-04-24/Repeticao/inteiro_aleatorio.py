from random import randint
from os import system


def limpar_console():
    system('cls')


def mostrar_resultado(numero, numero_sorteado, tentativas):
    if numero == numero_sorteado:
        print(f'Parabéns, você acertou o numero sorteado em {tentativas} vezes!')
    else:
        print(f'Não foi desta vez! {numero_sorteado}')


max = 10
tentativas = 0
numero_sorteado = randint(1, 100)
numero = 0

while (tentativas < max) and (numero_sorteado != numero):
    limpar_console()
    print(f'Você tem {max - tentativas}, chances!')
    numero = int(input('Adivinhe o numero sorteado(1 a 100):'))

    if numero > numero_sorteado:
        print(f'Numero sorteado é menor que {numero}')
    elif numero < numero_sorteado:
        print(f'Numero sorteado é maior que {numero}')

    tentativas += 1

mostrar_resultado(numero, numero_sorteado, tentativas)