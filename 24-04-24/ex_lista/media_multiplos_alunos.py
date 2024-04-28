def nota_valida(nota):
    return 0 <= nota <= 10


def obter_nota():
    try:
        nota = float(input('Nota: '))
        if nota_valida(nota):
            return nota
        print('\033[FNota: Inválida')
        return None
    
    except (ValueError, TypeError):
        print('\033[FNota: Inválida')
        return None


def registrar_notas_de_aluno():
    lista_notas = list()
    while len(lista_notas) < 4:
        nota = obter_nota()
        if not nota is None:
            lista_notas.append(nota)
    return lista_notas


def calcular_media(lista_com_notas):
    soma_notas = sum(lista_com_notas)
    quantidade_notas = len(lista_com_notas)
    media = soma_notas / quantidade_notas
    return media


def quantidade_alunos_aprovados(lista_com_medias):
    notas_aprovadas = [nota for nota in lista_com_medias if nota >= 7]
    return len(notas_aprovadas)


def main():
    total_repeticoes = 10
    total_medias = []
    for repeticao in range(1, total_repeticoes+1):
        print(f'\n{f" ALUNO {repeticao} ":=^60}')
        notas = registrar_notas_de_aluno()
        media = calcular_media(notas)
        total_medias.append(media)
    print(f'\nTotal de alunos APROVADOS: {quantidade_alunos_aprovados(total_medias)}')


if __name__ == "__main__":
    main()