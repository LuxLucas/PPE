def obter_frase():
    frase = input('Digite uma frase para contar as letras: ')
    return frase


def contar_caracteres(frase):
    caracteres_encontrados = {}
    for caractere in frase:
        if not caractere in caracteres_encontrados:
            caracteres_encontrados[caractere] = 1
        else:
            caracteres_encontrados[caractere] += 1
    return caracteres_encontrados


frase = obter_frase()
caracteres = contar_caracteres(frase)
print(caracteres)
