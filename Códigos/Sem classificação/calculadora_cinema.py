print('Olá! Vou calcular o quanto cada um gastou no cinema e para quem deve pagar.\nComplete os dados abaixo.')

quantas_pessoas = int(input('Quantas pessoas foram? '))

tipo_transporte_ida = input('Vocês foram de ônibus? (Sim/ Não) ')
if tipo_transporte_ida == Não:
    preço_transporte_ida = float(input('Quanto custou a viagem pelo aplicativo? (ida)'))
    quem_pagou1 = input('Insira o nome de quem pagou: ')

#print('Entendi! Quem pagou R${} foi {}.'.format(preço_transporte_ida, quem_pagou1))

tipo_transporte_volta = input('E vocês voltaram de ônibus? (Sim/ Não) ')
if tipo_transporte_volta == Não:
    preço_transporte_volta = float(input('Quanto foi a volta? '))
    quem_pagou2 = input('E quem pagou? ')

print('OK, entendi.')
preço_transporte = preço_transporte_ida + preço_transporte_volta
preço_transporte_unitário = preço_transporte / quantas_pessoas

if quem_pagou1 == quem_pagou2:
    print('''Confirme as informações: São {} pessoas, que gastaram R${} em transporte, pagos por {}.
Então cada uma das outras {} pessoas devem, até o momento, R${} para {}.'''.format(quantas_pessoas, preço_transporte, quem_pagou1,
                                                                         quantas_pessoas - 1, preço_trasnporte_unitário, quem_pagou1))

    

ingresso_inteira = float(input('Quanto custou a inteira? '))
ingresso_meia = ingresso_inteira / 2

ric = (preço_transporte_ida + preço_transporte_volta) / 3 + ingresso_inteira
raf = (preço_transporte_ida + preço_transporte_volta) / 3 + ingresso_meia
ota = (preço_transporte_ida + preço_transporte_volta) / 3 + ingresso_meia

ingresso_ric = float(input('Qual o preço do ingresso do Ricardo? '))

                     
