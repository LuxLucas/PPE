def obter_nome():
    nome = input('Seu nome: ')
    return nome


def validar_idade(idade):
    return not idade is None


def obter_idade():
    try:
        idade = int(input('Sua idade: '))
        if validar_idade(idade):
            return idade
        return None
    except (ValueError, TypeError) as erro:
        print(f'Erro: {erro}')
        return None


def obter_endereco():
    endereco = input('Seu endereço: ')
    return endereco


def obter_telefone():
    telefone = input('Seu telefone: ')
    return telefone


pessoa = {}
funcoes = {
    "nome": obter_nome,
    "idade": obter_idade,
    "endereco": obter_endereco,
    "telefone": obter_telefone
}
chavez = ["nome", "idade", "endereco", "telefone"]
tamanho_dicionario = len(pessoa)

while tamanho_dicionario < 4:
    chave = chavez[tamanho_dicionario]
    valor = funcoes[chave]()
    if not valor is None:
        pessoa[chave] = valor
        tamanho_dicionario = len(pessoa)

print(pessoa)