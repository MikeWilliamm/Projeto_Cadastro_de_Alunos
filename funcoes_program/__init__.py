def menu():
        opcoes = ['Visualizar cadastros.', 'Cadastrar usúario.', 'Sair do programa.']
        cabecalho('SISTEMA CADASTRO DE ALUNOS', '\033[1;32m')
        for c in range(len(opcoes)):
            print(f'\033[1;32m{c+1} - {opcoes[c]}\033[m')


def cabecalho(msg, cor = 'SEM COR'):
        if cor == 'SEM COR':
            print('-'*42)
            print(f'{msg}'.center(42))
            print('-'*42)
        else:
            print(f'{cor}-\033[m'*42)
            print(cor + str(msg).center(42) + '\033[m')
            print(f'{cor}-\033[m'*42)

def msgCor(msg, cor = '\033[1;31m'):
    return print(cor + msg + '\033[m')

def leiaINT():
    while True:
        
        try:
            resp = str(input('\033[1;33mSua Opção: \033[m'))
            resp = int(resp)
            
        except (ValueError, TypeError):
            msgCor('\033[1;31mDigite uma opção valida!\033[m')
            continue
        except KeyboardInterrupt:
            msgCor('\033[1;31m\nPor favor, escolha uma opção.\033[m')
            continue
        except Exception as erro:
            msgCor(f'\033[1;31mERRO: {erro}\033[m')
            continue
        else:
            break
    return resp        

def cadastra():
    nome = nota1 = nota2 = 0
    while True:
        try: 
            nome = str(input('\033[1;94mNome: \033[m')).strip()
            nome_teste = nome.replace(' ', '')
            if nome_teste.isalpha():
                break
            else:
                msgCor(f'{nome} Digite um nome valido!')
                continue
        except Exception as erro:
            msgCor('Digite um nome valido!')
            msgCor(f'ERRO: {erro}')
            continue
        except KeyboardInterrupt:
            msgCor('Digite um nome!')
            continue
    
    while True:
        try:
            nota1 = float(input('\033[1;94mNota 1: \033[m'))
            if nota1 < 0 or nota1 > 10:
                msgCor('Digite uma nota entre 0 e 10!')
                continue
            else:
                break
        except (ValueError, TypeError):
            msgCor('Digite uma nota valida!')
            continue
        except KeyboardInterrupt:
            msgCor('\nDigite a nota 1!')
        except Exception as erro:
            msgCor(f'ERRO: {erro}')
    
    while True:
        try:
            nota2 = float(input('\033[1;94mNota 2: \033[m'))
            if nota2 < 0 or nota2 > 10:
                msgCor('Digite uma nota entre 0 e 10!')
                continue
            else:
                break
        except (ValueError, TypeError):
            msgCor('Digite uma nota valida!')
            continue
        except KeyboardInterrupt:
            msgCor('\nDigite a nota 1!')
        except Exception as erro:
            msgCor(f'ERRO: {erro}')
    
    return nome, nota1, nota2