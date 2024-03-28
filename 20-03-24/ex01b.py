PrimeiroNumero = float(input('Primeiro número: '))
SegundoNumero = float(input('Segundo número: '))
Maior = PrimeiroNumero

if PrimeiroNumero < SegundoNumero:
    Maior = SegundoNumero

print(f'{"RESPOSTA":=^50}')
print(f'Maior número: {Maior}')