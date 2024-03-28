def Feedback(media):
    if media > 6:
        print(f'{'\033[32m'}Boa média{'\033[m'}')
    
    elif media > 5:
        print(f'{'\033[33m'}Precisa de recuperação{'\033[m'}')

    else:
        print(f'{'\033[31m'}Precisa melhorar a média{'\033[m'}')


Nota = []
Nota.append(float(input(f'Primeira NOTA: ')))
Nota.append(float(input(f'Segunda NOTA: ')))
Nota.append(float(input(f'Terceira NOTA: ')))

Media = sum(Nota)/3
Menor = min(Nota)
Maior = max(Nota)

print(f'{"RESULTADO":=^50}')
print(F'Média: {Media:.2f}')
print(F'Maior Nota: {Maior:.2f}')
print(F'Menor Nota: {Menor:.2f}')
Feedback(Media)