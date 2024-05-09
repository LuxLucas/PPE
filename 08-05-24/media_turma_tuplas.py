def calcular_media(notas):
    media = sum(notas)/len(notas)
    return media


# Declaração de variáveis
notas_primeira_prova = (7, 8.3, 10, 6.5, 9.3)
notas_segunda_prova = (8.5, 6.9, 5, 7.5, 9.8)
notas = [notas_primeira_prova, notas_segunda_prova]

# média das provas
medias = [calcular_media(notas_primeira_prova), calcular_media(notas_segunda_prova)]

# Mostra a média de cada prova
print(f'Média da turma na prova A: {medias[0]:.2f}')
print(f'Média da turma na prova B: {medias[1]:.2f}')

# Mostra a relação da turma com a média das provas
if medias[0] > medias[1]:
    print('A turma obteve a maior média na prova 1')
if medias[0] < medias[1]:
    print('A turma obteve a maior média na prova 2')
if medias[0] == medias[1]:
    print('A turma obteve a mesma média em ambas as provas')
