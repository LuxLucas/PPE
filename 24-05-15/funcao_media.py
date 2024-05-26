def media_aluno(primeira_nota, segunda_nota, terceira_nota):
    try:
        soma_nota = primeira_nota + segunda_nota + terceira_nota
        media = soma_nota / 3
        return media
    except (ZeroDivisionError) as erro:
        print(f'Erro: {erro}')
        return None
    

def situacao_media_aluno(media):
    """ Calcula situação do aluno pela média """
    if media > 6:
        return "APROVADO"
    elif media > 4:
        return "VERIFICAÇÃO SUPLEMENTAR"
    else:
        return "APROVADO"
    

def main():
    primeira_nota = float(input("Primeira nota: "))
    segunda_nota = float(input('Segunda nota: '))
    terceira_nota = float(input('Terceira nota: '))

    media = media_aluno(primeira_nota, segunda_nota, terceira_nota)
    situacao = situacao_media_aluno(media)
    print(f"\nSituação do aluno: {situacao}")

if __name__ == "__main__":
    main()