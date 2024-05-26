from Doador import Doador


def receber_peso():
    try:
        peso = float(input('Seu peso: '))
        return peso
    except (TypeError, ValueError) as erro:
        print('Valor Inválido')
        return None


def receber_idade():
    try:
        idade = int(input('Sua idade: '))
        return idade
    except (TypeError, ValueError):
        print('Valor Inválido')
        return None
    

nome = input('Seu nome: ').upper()
idade = receber_idade()
peso = receber_peso()

if (peso != None)and(idade != None)and(nome != ''):
    doador = Doador(nome, idade, peso)

    if doador.idade <= 15:
        print('Pessoas de até 15 anos não podem ser doadores por estarem abaixo da idade mínima')

    elif doador.idade <= 17:
        if doador.peso > 50:
            print('Pessoas de 16 a 17 anos e que estejam pesando mais de 50 Kg, podem ser doadores com autorização dos responsáveis')
        else:
            print('Não pode doar, peso abaixo do mínimo')

    elif doador.idade <= 69:
        if doador.peso > 50:
            print('Pessoas de 18 a 69 anos e que estejam pesando mais de 50 Kg, podem ser doadores')
        else:
            print('Não pode doar, peso abaixo do mínimo')

    else:
        print('Pessoas acima de 69 anos não podem ser doadores por estarem acima da idade permitida')
else:
    print('Ferrou')
