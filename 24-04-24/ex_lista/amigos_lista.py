from emoji import emojize

#Otto: Meu celular | Beto: Minha mochila | Max: Minha mala/bolsa | Kler: Meu notebook | Eva: Meus óculos
lista_amigos = ['Otto', 'Beto', 'Max', 'Kler', 'Eva']

for amigo in  lista_amigos:
    print(f'Obrigado por estar sempre comigo, {amigo}. {emojize(':feliz:', language='pt')}')