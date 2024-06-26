def validar_string(string):
    return not string is None


def obter_nome():
    nome = input('Nome: ').upper()
    return nome


def obter_nome_valido():
    while True:
        nome = obter_nome()
        if validar_string(nome):
            break
    return nome


def obter_funcao():
    funcao = input('Funçao: ').upper()
    return funcao


def obter_funcao_valido():
    while True:
        funcao = obter_funcao()
        if validar_string(funcao):
            break
    return funcao


def obter_tempo_servico():
    try:
        tempo_servico = float(input('Tempo de serviço: '))
        return tempo_servico
    except (TypeError, ValueError) as erro:
        print(f'Erro: {erro}')
        return None


def validar_tempo_servico(tempo_servico):
    return not tempo_servico is None


def obter_tempo_servico_valido():
    while True:
        tempo_servico = obter_tempo_servico()
        if validar_tempo_servico(tempo_servico):
            break
    return tempo_servico


def cadastrar_funcionario():
    nome = obter_nome_valido()
    funcao = obter_funcao_valido()
    tempo_servico = obter_tempo_servico_valido()
    funcionario = {'nome':nome, 'função':funcao, 'tempo_serviço':tempo_servico}
    return funcionario


def cadastrar_grupo_funcionarios():
    grupo = {}
    for index in range(6):
        print(f'\n{" CADASTRANDO FUNCIONÁRIO ":=^50}')
        funcionario = cadastrar_funcionario()
        grupo[index] = grupo.get(index, funcionario)
    return grupo


def validar_escolha_funcionario_para_demissao(indice_funcionario, grupo_funcionarios):
    return indice_funcionario in grupo_funcionarios.keys() 


def obter_indice_funcionario_para_demissao():
    try:
        indice = int(input('Índice de funcionário: '))
        return indice
    except (TypeError, ValueError) as erro:
        print(f'Erro: {erro}')
        return None


def obter_indice_de_funcionario_para_demissao_valido(grupo_funcionarios):
    indices = grupo_funcionarios.keys()
    print(f'\n{" DEMITIR FUNCIONÁRIO ":=^50}')
    print(f'Índices Válidos: {indices}')
    
    while True:
        indice_funcionario = obter_indice_funcionario_para_demissao()
        if validar_escolha_funcionario_para_demissao(indice_funcionario, grupo_funcionarios):
            break
    
    return indice_funcionario



def impedir_demissao(funcionario):
    return (funcionario['função'] == 'PROGRAMADOR') and (funcionario['tempo_serviço'] >= 3) 


def demitir_funcionario_se_valido(indice, grupo):
    if impedir_demissao(grupo[indice]):
        print('ERRO: USUÁRIO NÃO PODE SER DELETADO')
    else:
        del grupo[indice]
        print('Usuário Demitido')

def mostrar_indice_grupo_funcionario(grupo):
    indices = []
    for index_funcionario in grupo.keys():
        indices.append(index_funcionario)
    return indices

grupo_funcionario = cadastrar_grupo_funcionarios()
funcionario_escolhido = obter_indice_de_funcionario_para_demissao_valido(grupo_funcionario)
demitir_funcionario_se_valido(funcionario_escolhido, grupo_funcionario)
print(f'Funcionários restantes: {mostrar_indice_grupo_funcionario(grupo_funcionario)}')