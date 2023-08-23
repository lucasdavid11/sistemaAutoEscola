import pandas as pd
import datetime

aulasrestantes = []
linhaAulaHoje = 0


table = pd.read_csv("AULAS_AUTO_ESCOLA.csv")#LEITURA DO ARQUIVO CSV
table['DATA'] = pd.to_datetime(table['DATA'], format='mixed')#TRANSFORMA COLUNA 'DATA'(STRING) EM TIPO DATA

tamanho = len(table['DATA'])

hoje = datetime.date.today()
hoje = pd.to_datetime(hoje, format='mixed')


for i in range(0, tamanho):#ARMAZENA AULAS FUTURAS NO VETOR AULASRESTANTES
    diferenca = (table['DATA'][i] - hoje).days
    if diferenca > 0:
        aulasrestantes.append(table['DATA'][i])
    if diferenca == 0:#VERIFICA SE HÁ AULA NA DATA DE HOJE
        linhaAulaHoje = i

if table["DATA"][linhaAulaHoje - 1] == table["DATA"][linhaAulaHoje]:
    linhaAulaHoje -= 1

menor = aulasrestantes[0]
for i in aulasrestantes:#VERIFICA A AULA MAIS PRÓXIMA NO VETOR AULASRESTANTES
    if i < menor:
        menor = i
    proximaAula = menor

if linhaAulaHoje:#SCRIPT PARA AULA HOJE
    print(
        f'Você possui aula hoje:\n{table["DATA"][linhaAulaHoje]} das {table["HORÁRIO"][linhaAulaHoje]} na categoria {table["CATEGORIA"][linhaAulaHoje]}')

    if table["DATA"][linhaAulaHoje] == table["DATA"][linhaAulaHoje + 1]:#CASO HAJA MAIS DE UMA AULA NO DIA ELE INFORMA TAMBÉM
        print(
            f'E a segunda aula:\n{table["DATA"][linhaAulaHoje + 1]} das {table["HORÁRIO"][linhaAulaHoje + 1]} na categoria {table["CATEGORIA"][linhaAulaHoje + 1]}')

    presenca = str(
        input(f'Sua presença consta como "{table["PRESENÇA"][linhaAulaHoje]}", você compareceu a esta aula?[S/N]'))

    while presenca not in 'NnSs':
        presenca = str(input('Erro! Digite [S/N]'))

    if presenca in 'Ss':#MARCA PRESENCA EM UMA OU DUAS AULAS CASO HAJA NO MESMO DIA
        table.loc[linhaAulaHoje, 'PRESENÇA'] = 'SIM'
        if table["DATA"][linhaAulaHoje] == table["DATA"][linhaAulaHoje + 1]:
            table.loc[linhaAulaHoje + 1, 'PRESENÇA'] = 'SIM'
    elif presenca in 'Nn':
        table.loc[linhaAulaHoje, 'PRESENÇA'] = 'NÃO'
        if table["DATA"][linhaAulaHoje + 1] == table["DATA"][linhaAulaHoje]:
            table.loc[linhaAulaHoje + 1, 'PRESENÇA'] = 'NÃO'

    print(f'Ok! Já atualizei sua presença na tabela de aulas!\n')

for i in range(0, tamanho):#VERIFICA PROXIMA AULA
    if table['DATA'][i] == proximaAula:
        linhaProximaAula = i
        break

print(
    f'Sua próxima aula será no dia:\n{table["DATA"][linhaProximaAula]} das {table["HORÁRIO"][linhaProximaAula]} na categoria {table["CATEGORIA"][linhaProximaAula]}')

if table["DATA"][linhaProximaAula + 1] == table["DATA"][linhaProximaAula]:#VERIFICA SE HÁ DUAS AULAS NO MESMO DIA DA PRÓXIMA AULA E INFORMA AS DUAS
    print(
        f'E a segunda aula:\n{table["DATA"][linhaProximaAula + 1]} das {table["HORÁRIO"][linhaProximaAula + 1]} na categoria {table["CATEGORIA"][linhaProximaAula + 1]}')

table.to_csv('AULAS_AUTO_ESCOLA.csv', encoding='utf-8', index=False)#SALVA ARQUIVOS CSV

verTabela = str(input('Deseja ver a tabela de aulas?[S/N]'))

while verTabela not in 'NnSs':
    verTabela = str(input('Erro! Digite [S/N]'))

if verTabela in 'Ss':
    print(table)#MOSTRA TABELA CSV
