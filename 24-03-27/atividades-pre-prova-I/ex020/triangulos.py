from os import system

def limpar_console():
    system('cls')

def is_triangle(PrimeiroLado, SegundoLado, TerceiroLado):
    Lados = [PrimeiroLado, SegundoLado, TerceiroLado]
    MaiorLado = max(Lados)
    Lados.remove(MaiorLado)
    return MaiorLado < sum(Lados)

def type_triangule(PrimeiroLado, SegundoLado, TerceiroLado):
    Lados = [PrimeiroLado, SegundoLado, TerceiroLado]
    if is_triangle(PrimeiroLado, SegundoLado, TerceiroLado):
        if max(Lados) == min(Lados):
            return "Equilátero" 
        
        if Lados[0] != Lados[1] != Lados[2]:
            return "Escaleno"
        
        if Lados[0] == Lados[1] or Lados[0] == Lados[2]:
            return "Isósceles"
    else:
        return "Não existe"
    
def main():
    limpar_console()
    LadosTriangulo = []
    try:
        for indice in range(3):
            LadosTriangulo.append(float(input(f'Lado {indice+1} do triângulo: ')))
    except (TypeError, ValueError) as Erro:
        print(f'\nErro: {Erro}') 
    valida_triangulo = is_triangle(LadosTriangulo[0], LadosTriangulo[1], LadosTriangulo[2])
    tipo_triangulo = type_triangule(LadosTriangulo[0], LadosTriangulo[1], LadosTriangulo[2])
    print(f'{"RESULTADO":=^60}')
    print(f'É um triãngulo ?: {valida_triangulo}')
    print(f'Tipo do triângulo: {tipo_triangulo}')


if __name__ == '__main__':
    main()
