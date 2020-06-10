# Ler nome e média de um aluno, guardar em um dicionário com a sua situação

aluno = {}  # podia escrever tudo em uma linha
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
aluno['situação'] = 'aprovado' if aluno['media'] >= 6 else 'reprovado'
print(f'{aluno["nome"]}, você está {aluno["situação"]}, pois sua média é {aluno["media"]}')

# Feito. Ok