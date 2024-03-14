#   Área de uma coroa
import math

RaioMaior = float(input('Digite o valor do raio maior: '))
RaioMenor = float(input('Digite o valor do raio menor: '))

AreaCoroa = math.pi * (RaioMaior ** 2 - RaioMenor ** 2)

print(f'Area da coroa circular é {AreaCoroa:,.2f}')
