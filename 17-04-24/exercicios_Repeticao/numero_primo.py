from math import  sqrt

def receberNumeroInteiro():
    try:
        NumeroInteiro = int(input('Digite um número inteiro: '))
        return NumeroInteiro
    except (TypeError, ValueError) as Erro:
        print(f'Erro: {Erro}')


def isPrimo(Numero):
    RaizQuadradaArredondadaPraCima = round(sqrt(Numero))
    multiplosEncontrados = 0
    for contador in range(1, RaizQuadradaArredondadaPraCima+1):
        if Numero % contador == 0:
            multiplosEncontrados += 1
    return multiplosEncontrados == 1 and Numero != 1


def main():
    NumeroDoUsuario = receberNumeroInteiro()
    print(f'Número é primo ?: {isPrimo(NumeroDoUsuario)}')


if __name__ == '__main__':
    main()