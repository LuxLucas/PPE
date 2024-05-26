def soma_looping(numero):
    numero -= 1
    if numero == 0 :
        return numero
    return numero + soma_looping(numero)

numero = int(input('Digite seu número: '))
soma_anteriores = soma_looping(numero)
print(soma_anteriores)