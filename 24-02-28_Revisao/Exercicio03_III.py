def confirmarResposta():
    print(f'\n{"PERGUNTA":=^50}')
    resposta = float(input('Dseja continuar ? (1:SIM/2:NÃO): '))
    if resposta == 1:
        print(f'{"\n"}')
        return True
    else:
        return False

print(f'\n{"DIVIDINDO":=^50}')
UserMessage = True
while UserMessage:
    while True:
        try:
            Dividendo = float(input('Digite seu dividendo número: '))
            Divisor = float(input('Digite seu divisor número: '))
            RespostaDivisao = Dividendo/Divisor
            break
        except (ValueError, ZeroDivisionError, TypeError) as erro:
            print('Erro:', erro)
    print(f'\n{"RESPOSTA":=^50}')
    print('Seu dividendo: {}\nSeu divisor: {}\nO resultdo de sua divisão é {:.2f}\n'.format(Dividendo, Divisor, RespostaDivisao))
    UserMessage = confirmarResposta()
