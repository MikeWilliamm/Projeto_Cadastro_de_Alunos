#https://www.youtube.com/watch?v=JXp-K-YENLs&list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h&index=7
from cProfile import label
from cgitb import text
from struct import pack
from tkinter import *

def  tela(janela):
    #Tamanho da Janela
    largura = 1200
    altura = 500
    #resolução do monitor
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    #posição da janela
    posx = int(largura_tela/2 - largura/2)
    posy = int(altura_tela/2 - altura/2)
    janela.geometry(f'{largura}x{altura}+{posx}+{posy}') #altera tamanho e posição inicial da janela 'larguraxaltura+posição1+posição2
    janela.resizable(False, False) #habilita se a altura e largura da janela pode ser redimencionada

    janela['bg'] = 'dodger blue'

    #alterar icone do programa
    #janela.iconphoto(True, PhotoImage(file="imagens/icone_mario - Copia.png")) 

    #ALTERANDO INTEFACE
    


def visualizar_alunos():
    janela.lower()
    newWindow = Toplevel()

    tela(newWindow)
    
    botao = Button(newWindow, text='Voltar ao menu', bg='dodger blue3',fg='black',font='Times 16', bd = 2,relief='solid',width=40, height=1, justify= LEFT, anchor=W,command=lambda: newWindow.destroy()) #passar a função no command sem os '()', assim ela será executada  somente quando clicar no botão
    botao.place(x=180, y= 80)
    import funcoes_DB as fdb
    fdb.selec()

#sempre que for fazer uma interface grafica, a primeira coisa é criar a janela principal
def botao_teste(msg):
    retorno['text'] = msg
    retorno2['text'] = msg
    retorno3['text'] = msg
    retorno4['text'] = msg
    retorno5['text'] = msg
    
janela = Tk() #começa janela

janela.title('SISTEMA DE ALUNOS') #Titulo do programa
tela(janela)

#ALTERANDO INTEFACE
# altera a cor de fundo bg = back ground
janela['bg'] = 'dodger blue' 
cabecalho = Label(janela, text='AAA',bg='dodger blue',fg='black',font='Times', bd = 10,relief='sunken', width=15, height=1) 
cabecalho.place(x=500, y=0)
#Um texto na janela
texto_menu = Label(janela, text='Menu de opções: ',bg='dodger blue',fg='black',font='Times 16', bd = 2,relief='solid',width=13, height=2) 
texto_menu.place(x=10, y=80)

botao = Button(janela, text='Visualizar cadastros de alunos', bg='dodger blue3',fg='black',font='Times 16', bd = 2,relief='solid',width=40, height=1, justify= LEFT, anchor=W,command=lambda: visualizar_alunos()) #passar a função no command sem os '()', assim ela será executada  somente quando clicar no botão
botao.place(x=180, y= 80)
botao2 = Button(janela, text='Cadastrar aluno', bg='dodger blue3',fg='black',font='Times 16', bd = 2,relief='solid',width=40, height=1, justify= LEFT, anchor=W,command=lambda: botao_teste('João\nMike\nWilliam')) #passar a função no command sem os '()', assim ela será executada  somente quando clicar no botão
botao2.place(x=180, y= 125)
# botao.pack()
# botao.grid(column=0, row= 1, padx=10, pady=10)

#no final da função que o botão chamou, será editado o text
#1-Tela usada, Text = que irá aparecer, bg = cor de fungo, fg = font, tamanho e parm, width = largura, height altura, bd = borda preta, relief = tipo da borda, anchor = alinhamento do texto dentro da borda [N,S,W,E] ou CENTER, justify = ALINHAMENTO DO TEXTO CENTER, RIGHT, LEFT
# retorno = Label(janela, text="",bg='red', fg='black', font='Arial 12 italic', width=30, height=5, bd = 5,relief='solid', anchor=NW, justify= LEFT)
# retorno2 = Label(janela, text="",bg='dodger blue', fg='black', font='Times 12 bold',bd = 10,relief='flat')
# retorno3 = Label(janela, text="",bg='dodger blue', fg='black', font='Verdana 12 italic',bd = 10,relief='raised')
# retorno4 = Label(janela, text="",bg='dodger blue', fg='black', font='Verdana 12 italic',bd = 10,relief='sunken')
# retorno5 = Label(janela, text="",bg='dodger blue', fg='black', font='Verdana 12 italic',bd = 10,relief='groove',anchor=S)
# retorno.pack()
# retorno2.pack()
# retorno3.pack()
# retorno4.pack()
# retorno5.pack()
# # retorno.grid(column=0, row=2, padx=10, pady=15)

janela.mainloop()#mainloop é para que a janela se mantenha aberta, sempre será minha ultima linha de código