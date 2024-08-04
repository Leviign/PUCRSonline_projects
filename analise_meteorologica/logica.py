#ENTRADA E VALIDAÇÃO DO USUÁRIO.
print('Informe para o ano de [...] as temperaturas máximas para seus meses')

qnt_meses_escaldates = 0
mes_mais_escaldante = 0
mes_menos_quente = 0
soma = 0
temp_anterior = 1
temp_atual = 0

for mes in range(1,13):
    temp = float(input(f'Temperatura máxima do mês {mes}: '))
    if temp < -60 or mes > 60:
        print('temperatura informada fora do esperado, verifique e digite novamente')
        break
    else: 
        if temp > 33: #QUANTIDADE DE MESES ESCALDANTES
            qnt_meses_escaldates = qnt_meses_escaldates + 1
        if temp_atual < temp_anterior: #COMPARANDO PARA ACHAR O MES MENOS QUENTE
            mes_menos_quente = mes
            temp_atual = temp
        if temp > temp_anterior: #COMPARANDO PARA ACHAR O MES MAIS QUENTE
            mes_mais_escaldante = mes
            temp_anterior = temp
    soma = soma + temp #CALCULO DA MÉDIA MÁXIMA ANUAL
    media =  soma/12        
#SAÍDAS PARA O USUÁRIO
print(f'\nquantidade de meses escaldantes: {qnt_meses_escaldates}')
print(f'mes mais escaldante do ano: {mes_mais_escaldante}')
print(f'Média máxima anual: {media:.2f}')
print(f'mês menos escaldante: {mes_menos_quente}')