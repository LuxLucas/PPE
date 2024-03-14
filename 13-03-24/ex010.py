#   Cálculo de vazão de volume
import math

def Receber_Dados_Tubo():
    Raio = float(input('Raio do tubo em METROS: '))
    Altura = float(input('Altura do tubo em METROS: '))
    Area = (math.pi * (Raio ** 2)) * Altura

    return Area

def Receber_Vazao_Tubo():
    Vazao = float(input('Tempo de vazão em HORAS: '))

    return Vazao

def Calcular_Vazao(area, vazao):
    vazao = area / vazao

    return vazao


while True: 

    Resposta = int(input('\nVocê sabe o volume do tubo ? (SIM: 1 || NÃO: 2): '))

    if Resposta == 1:
        print(f'{"RECEBENDO DADOS":=^50}')
        Volume = float(input('Informe o volume em METROS: '))
        Tempo = Receber_Vazao_Tubo()
        Vazao = Calcular_Vazao(Volume, Tempo)
        break

    elif Resposta == 2:
        print(f'{"RECEBENDO DADOS":=^50}')
        Volume = Receber_Dados_Tubo()
        Tempo = Receber_Vazao_Tubo()
        Vazao = Calcular_Vazao(Volume, Tempo)
        break

    else:
        print('CARACTÉRE INVÁLIDO')

print(f'{"DADOS PROCESSADOS":=^50}')
print(f'Sua vazão é de {Vazao} m³/s', end='\n')
