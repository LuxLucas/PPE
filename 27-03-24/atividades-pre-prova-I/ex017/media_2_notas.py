from os import system

def limpar_console():
    system('cls')

def media_notas(PrimeiraNota, SegunaNota):
    return (PrimeiraNota + SegunaNota)/2

def situacao_aluno(PrimeiraNota, SegunaNota):
    Media = media_notas(PrimeiraNota, SegunaNota)
    if Media == 10:
        return "APROVADO COM DISTINÇÃO"
    elif Media >= 7:
        return "APROVADO"
    else:
        return "REPROVADO"

def main():
    limpar_console()
    Notas = []
    try:
        for indice in range(2):
            Notas.append(float(input(f'Nota {indice+1}: ')))
    except (TypeError, ValueError) as Erro:
        print(f'\nErro: {Erro}')
    
    print(F'{"RESPOSTA":=^60}')
    print(situacao_aluno(Notas[0], Notas[1]))

if __name__  == '__main__':
    main()