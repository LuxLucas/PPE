def criar_funcionario(nome = 'Anônimo', salario = 9000):
    return {"nome": nome, "salario":salario}


def obter_salario():
    try:
        salario = float(input('Salário'))
        return salario
    except (TypeError, ValueError):
        return None

nome = input('Nome: ')
salario =  obter_salario()

if not salario is None:
    funcionario = criar_funcionario(nome, salario)
else:
    funcionario = criar_funcionario(nome)
    
print(funcionario)