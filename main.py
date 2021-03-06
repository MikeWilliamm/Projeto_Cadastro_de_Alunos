#from funcoes_program import * #método de importação.
import funcoes_program as fp
import funcoes_DB as fdb
from time import sleep

#Função para salvar log, todos os prints devem ser chamados com ela.
# def print_msg(msg):
#     with open('log.txt', 'w+') as file:
#         file.write(msg)
#     print(msg)

while True:
    fp.menu()
    resp = fp.leiaINT()

    while resp not in [1,2,3,4,5]:
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
    if resp == 3:
        try:
            print('-'*42)
            alunos = fdb.selec()
            print('-'*42)
            id = int(input('\033[1;94mDigite o "ID" do aluno que deseja deletar [999 para cancealar]: \033[m'))
            while True:
                for i in alunos:
                    verifica = 0
                    if i[0] == id or id == 999:
                        if id == 999:
                            fp.msgCor('Operação canceçada!','\033[1;94m')
                            verifica = 1
                            break
                        else:
                            fdb.deleta(id)
                            verifica = 1
                            break
                if verifica == 1:
                    break
                else:
                    fp.msgCor('ERRO! Digite um ID valido')
                    id = int(input('\033[1;94mDigite o "ID" do aluno que deseja deletar [999 para cancealar]: \033[m'))

                
        except Exception as erro:
            print(erro)
            
    if resp == 4:
        fp.msgCor('Exportando registro para um csv.','\033[1;94m')
        fdb.exportaCSV()
    if resp == 5 :
        fp.cabecalho('PROGRAMA FINALIZADO', '\033[1;32m')
        break

