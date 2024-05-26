import os
from time import sleep


def limpar():
    os.system('cls')


def autenticar_palavra(palavra, frase):
    if not palavra in frase:
        limpar()
        print(f'\n{cores["vemelho"]}{"CARACTERE INVÁLIDO":=^60}{cores["normal"]}')
        sleep(3)
        return False
    else:
        return True


cores = {
    'normal': '\033[m',
    'vemelho': '\033[31m'
}

while True:
    Frase = input(f'Uma frase: ')
    PalavraAntiga = input(f'Uma palavra da frase: ')

    if autenticar_palavra(PalavraAntiga, Frase):
        PalavraNova = input(f'Uma nova palavra: ')
        break

print(f'\nFrase Antiga: {Frase}')
FraseNova = Frase.replace(PalavraAntiga, PalavraNova)
print(f'Frase Nova: {FraseNova}')

        