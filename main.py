2
#from funcoes_program import * #método de importação.
import funcoes_program as fp
import funcoes_DB as fdb
from time import sleep

while True:
    fp.menu()
    resp = fp.leiaINT()

    while resp not in [1,2,3]:
        print(f'\033[1;31mA opção {resp} é invalida!\033[m')
        sleep(1)
        fp.menu()
        resp = fp.leiaINT()

    if resp == 1:
        print('-'*42)
        alunos = fdb.selec()
        print('-'*42)
        resp = str(input('\033[1;94mDeseja visualisar as notas de algum aluno? [S/N]: \033[m')).strip().upper()

        while resp != 'S' and resp != 'N':
            fdb.msgCor('Digito Invalido!!!')
            resp = str(input('\033[1;94mDeseja visualisar as notas de algum aluno? [S/N]: \033[m')).strip().upper()
        
        if resp == 'S':
            
            while True:
                try:
                    id = str(input('\033[1;94mDigite o ID do aluno: \033[m'))
                    id = int(id)
                    contador = verifica = 0
                    for i in alunos:
                        if i[0] == id:
                            print('-'*42)
                            fdb.msgCor(f'{"ID.":<5}{"Nome":<17}{"Nota1":<8}{"Nota2":<8}','\033[1;94m')
                            fdb.msgCor(f'{i[0]:<5}{i[1]:<17}{i[2]:<8}{i[3]:<8}','\033[1;94m')
                            print('-'*42)
                            verifica = 1
                        elif contador+1 == len(alunos) and verifica == 0:
                            fp.msgCor('ID não encontado!!!')
                        contador += 1
                        
                except Exception as erro:
                    fdb.msgCor('ERRO!!! Digite um inteiro valido!')
                    print(erro)
                else:
                    resp = str(input('\033[1;94mDeseja visualisar as notas de outro aluno? [S/N]: \033[m')).strip().upper()

                    while resp != 'S' and resp != 'N':
                        fdb.msgCor('Digito Invalido!!!')
                        resp = str(input('\033[1;94mDeseja visualisar as notas de outro aluno? [S/N]: \033[m')).strip().upper()
                    
                    if resp == 'N':
                        break

    if resp == 2:
        fp.cabecalho('CADASTRAR USÚARIO','\033[1;94m')
        nome, nota1, nota2 = fp.cadastra()
        try:
            fdb.importa(nome, nota1, nota2)
            continue
        except:
            continue
    if resp == 3 :
        fp.cabecalho('PROGRAMA FINALIZADO', '\033[1;32m')
        break