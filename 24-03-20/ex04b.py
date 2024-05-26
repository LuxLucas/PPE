Palavra = input(f'Digite uma letra: ').upper()

if Palavra.isalpha():
    if Palavra in ['A', 'E', 'I', 'O', 'U']:
        print(f'{Palavra} é uma VOGAL')
    else:
        print(f'{Palavra} é uma CONSOANTE')
else:
    print(f'Essa "LETRA" não está nos grupos listados')
