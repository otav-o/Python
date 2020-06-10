# Crie uma função que leia o ano de nascimento e diga se o voto é obrigatório, opcional ou se a pessoa não vota.

def votacao(nasc):
    from datetime import date       # "economia de memória" - escopo de importação

    idade = date.today().year - nasc
    if idade < 16:
        situacao = 'NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        situacao = 'VOTO OPCIONAL.'
    elif 18 <= idade < 65:
        situacao = 'VOTO OBRIGATÓRIO.'
    print(f'Pessoa com {idade} anos: {situacao}')


while True:
    ano = int(input('Digite o ano de nascimento: '))
    votacao(ano)
    perg = input('Deseja continuar? ').strip().upper()[0]
    if perg == 'N':
        break

# Feito. Ok