import psycopg2
def msgCor(msg, cor = '\033[1;31m'):
    return print(cor + msg + '\033[m')

def conexao():
    try:
        connection_data = psycopg2.connect(host = 'localhost', database = 'testedb', user = 'postgres', password = '154878', port = 5432) 
        cur = connection_data.cursor()
    except Exception as erro:
        msgCor(f'PROBLEMA AO SE CONECTAR AO DB!')
        connection_data.rollback()
    else:
        return connection_data, cur

    

def importa(nome, nota1, nota2):
        try: 
            connection_data, cur = conexao()
            sql = f"insert into alunos (nome, nota1, nota2) values('{nome}', {nota1}, {nota2})"
            
            cur.execute(sql)
            connection_data.commit()
            msgCor(f'DADOS CADASTRADOS.','\033[1;94m')
        except Exception as erro:
            connection_data.rollback()
            msgCor(f'ERRO NO COMANDO INSERT!')

def selec():
    try: 
        connection_data, cur = conexao()
        sql = f'select * from alunos;'
        cur.execute(sql)
        alunos = cur.fetchall()
        msgCor(f'{"ID.":<5}{"Nome":<17}{"Média":>5}','\033[1;94m')
        for i in alunos:
            msgCor(f'{i[0]:<5}{i[1]:<17}{(i[2] + i[3])/2:>5}','\033[1;94m')
        return alunos
    except:
        connection_data.rollback()
        msgCor('ERRO AO TENTAR VISUALIZAR USÚARIOS CADASTRADOS!')
    
        