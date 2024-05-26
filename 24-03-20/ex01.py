PrimeiroPlanoX, PrimeiroPlanoY = float(input(f'X¹: ')), float(input(f'Y¹: '))
SegundoPlanoX, SegudoPlanoY = float(input(f'\nX²: ')), float(input(f'Y²: '))

Distancia = ((SegundoPlanoX - PrimeiroPlanoX)**2 + (SegudoPlanoY - PrimeiroPlanoY)**2)**(1/2)

print(f'Resultado: {Distancia}')