import mysql.connector
from mysql.connector import Error
import tkinter
import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno

# Variáveis globais
global hostX, userX, passwordX, databaseX, cursorX
global comando_sql_criar_database, comando_sql_criar_table,  comando_sql_inserir, comando_sql_select, comando_sql_seguranca, comando_sql_deletar
global caixa_combo_diasX, caixa_combo_mesesX, caixa_combo_anosX

global fonte_tela, fonte_label
global path_foto, img_bt_inserir, img_bt_excluir
 
# Dados para conexão com o banco de dados
hostX = 'localhost'
userX = 'root'
passwordX = 'acesso123'
databaseX = 'academico'

fonte_tela = 'Roboto'
fonte_label = 'Roboto'

# Instruções SQL (não mexer)
comando_sql_criar_database = "CREATE DATABASE IF NOT EXISTS academico"

# Alterar conforme dados do banco de dados
comando_sql_criar_table = "CREATE TABLE IF NOT EXISTS `usuarios` (`id_user` INT NOT NULL AUTO_INCREMENT, `nome_user` VARCHAR(50) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL, `path_foto_user` VARCHAR(200) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL, `data_user` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,`senha_user` VARCHAR(30) NOT NULL, PRIMARY KEY (`id_user`))"

# Alterar conforme dados do banco de dados
comando_sql_inserir = "INSERT INTO usuarios (nome_user, path_foto_user, data_user, senha_user) VALUES(%s, %s, %s, %s)"
comando_sql_select = "SELECT * FROM usuarios;"
comando_sql_seguranca = "SET SQL_SAFE_UPDATES = 0;"
comando_sql_deletar = "DELETE FROM usuarios WHERE id_user = %s;"

caixa_combo_diasX = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
caixa_combo_mesesX = ['01','02','03','04','05','06','07','08','09','10','11','12']
caixa_combo_anosX = ["1900","1901","1902","1903","1904","1905","1906","1907","1908","1909","1910","1911","1912","1913","1914","1915","1916","1917","1918","1919","1920","1921","1922","1923","1924","1925","1926","1927","1928","1929","1930","1931","1932","1933","1934","1935","1936","1937","1938","1939","1940","1941","1942","1943","1944","1945","1946","1947","1948","1949","1950","1951","1952","1953","1954","1955","1956","1957","1958","1959","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006"]

# Lista de mensagens
mensagem_bd = ['Erro de Conexão ao banco de dados.',
               'Erro ao criar banco de dados.',
               'Erro ao criar tabela no banco de dados.',
               'Registro cadastrado com sucesso',
               'Erro ao cadastrar o registro',
               'Erro ao deletar o cadastro',
               'Deseja deletar o registro selecionado?']

fonte_label = 'Old English Text MT'
cor1 = '#fa0202'

# Função para conectar o banco de dados.
def conectar():
    global banco
    try:
        banco = mysql.connector.connect(
            host = hostX, 
            user = userX,
            password = passwordX)
        #print('Conexão 0: ', banco)
    except Error as erro:
        print(mensagem_bd[0])
            
# Função para criar o banco de dados
def criar_database():
    global banco
    try:
        conectar()
        cursorX = banco.cursor()
        cursorX.execute(comando_sql_criar_database)        
    except Error as erro:
        print(mensagem_bd[1])
        
    if banco.is_connected():
        cursorX.close()

# Função para criar tabela
def criar_tabela():
    global banco
    try:
        banco = mysql.connector.connect(
            host = hostX,
            user = userX,
            password = passwordX,
            database = databaseX
        )

        cursorX = banco.cursor()
        cursorX.execute(comando_sql_criar_table)
        print(banco)
    except Error as erro:
        print(mensagem_bd[2])
        
    if banco.is_connected():
            banco.close()

def salvar_vendas():
    messagebox.showinfo(title='Salvar', message='Você clicou no botão de Salvar')

def excluir_vendas():
    messagebox.showwarning(title='Exclusão', message='Você clicou no botão de Excluir')

janela = Tk()
janela.title('Sistema acadêmico')
janela.geometry('850x385')

janela.configure(bg='white')
janela.resizable(width=FALSE, height=FALSE)

# JANELA 
barrastatus = tk.Label(janela, text="Cadastro de Produtos", bd=1, relief=tk.SUNKEN, anchor=tk.W)
barrastatus.pack(side=tk.TOP, fill=tk.X)

label_cadastro = Label(janela, text='Produtos', fg=cor1, bg='white', font=(fonte_label,'30'), justify='center')
label_cadastro.pack(side=TOP)

# FRAME 1 
label_cod = Label(janela, text='Código', fg='blue', bg='white', font=(fonte_label,'14'))
label_cod.place(x=110,y=80)
entry_cod = Entry(janela, font=('Arial','12'), relief='solid')
entry_cod.place(x=175, y=82, height=28)
entry_cod['state'] = 'disabled'

label_desc = Label(janela, text='Descrição', fg='blue', bg='white', font=(fonte_label,'14'))
label_desc.place(x=90, y=120)
entry_desc = Entry(janela, font=('Arial','12'), relief='solid')
entry_desc.place(x=175,y=122,height=28)

label_type = Label(janela, text='Tipo do Produto', fg='blue', bg='white', font=(fonte_label,'14'))
label_type.place(x=40,y=160)
entry_type = Entry(janela, font=('Arial','12'), relief='solid')
entry_type.place(x=175,y=162,height=28)

label_data = Label(janela, text='Data ', fg='blue', bg='white', font=(fonte_label,'14'))
label_data.place(x=127,y=200)
escolher_dia = StringVar()
caixa_combo_dias = ttk.Combobox(janela, textvariable=escolher_dia)
caixa_combo_dias['values']=caixa_combo_diasX
caixa_combo_dias.place(x=175, y=200, width=45, height=28)

escolher_meses = StringVar()
caixa_combo_meses = ttk.Combobox(janela, textvariable=escolher_meses)
caixa_combo_meses['values']=caixa_combo_mesesX
caixa_combo_meses.place(x=230, y=200, width=45, height=28)

escolher_anos = StringVar()
caixa_combo_anos = ttk.Combobox(janela, textvariable=escolher_anos)
caixa_combo_anos['values']=caixa_combo_anosX
caixa_combo_anos.place(x=285, y=200, width=45, height=28)

label_valor = Label(janela, text='Valor', fg='blue', bg='white', font=(fonte_label,'14'))
label_valor.place(x=118,y=240)
entry_valor = Entry(janela,font=('Arial','12'), relief='solid')
entry_valor.place(x=175,y=242,height=28)

label_user = Label(janela, text='Usuário', fg='blue', bg='white', font=(fonte_label,'14'))
label_user.place(x=100,y=280)
entry_user = Entry(janela,font=('Arial','12'), relief='solid')
entry_user.place(x=175,y=282,height=28)

img_bt_inserir=PhotoImage(file = r"Salvar.png") 
img_bt_excluir=PhotoImage(file = r"Excluir.png")

botao_inserir = Button(janela,text='', image=img_bt_inserir, compound = LEFT, command=salvar_vendas, relief='groove', font=(fonte_label,'14'), fg='black')
botao_inserir.place(x=650,y=335,width=80,height=30)

botao_excluir = Button(janela,text='', image=img_bt_excluir, compound = LEFT, command=excluir_vendas, font=(fonte_label,'14'), relief='groove', fg='black')
botao_excluir.place(x=750,y=335,width=80,height=30)

janela.mainloop()