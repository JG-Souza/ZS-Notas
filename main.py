import customtkinter as ctk
from CTkTable import *
import sqlite3
from api import persiste_dados

# Criando janela
app = ctk.CTk()
app.geometry('800x800')
app.title('Notas Mimi')


# Iniciando meu DB

con = sqlite3.connect('data.db', check_same_thread= False)
query_criar_tabela = '''CREATE TABLE IF NOT EXISTS boletim
(id INT AUTO INCREMENT, materia TEXT, notaref TEXT, nota INT)
'''
con.execute(query_criar_tabela)
cursor = con.cursor()


# Criando a classe

class Materia:
    def __init__(self, nome, notas, total, falta):
        self.nome = nome
        self.notas = notas
        self.total = total
        self.falta = falta

# Criando os objetos (Matérias)

m1 = Materia('Matemática', list(), 0, 7)
m2 = Materia('Biologia', list(), 0, 7)
m3 = Materia('Física', list(), 0, 7)
m4 = Materia('Química', list(), 0, 7)
m5 = Materia('Português', list(), 0, 7)
m6 = Materia('Literatura', list(), 0, 7)
m7 = Materia('Espanhol', list(), 0, 7)
m8 = Materia('Inglês', list(), 0, 7)
m9 = Materia('História', list(), 0, 7)
m10 = Materia('Geografia', list(), 0, 7)
m11 = Materia('Sociologia', list(), 0, 7)
m12 = Materia('Filosofia', list(), 0, 7)

# Valores da minha tabela

value = [['Matéria', 'Av1', 'Av2', 'Av3', 'Av4', 'Av5', 'Total', 'Falta'],
             ['Mat', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n5']).fetchone(), m1.total, m1.falta],
             ['Bio', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n5']).fetchone(), m2.total, m2.falta],
             ['Fis', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n5']).fetchone(), m3.total, m3.falta],
             ['Qui', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n5']).fetchone(), m4.total, m4.falta],
             ['Port', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n5']).fetchone(), m5.total, m5.falta],
             ['Lit', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n5']).fetchone(), m6.total, m6.falta],
             ['Esp', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n5']).fetchone(), m7.total, m7.falta],
             ['Ing', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n5']).fetchone(), m8.total, m8.falta],
             ['Hist', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n5']).fetchone(), m9.total, m9.falta],
             ['Geo', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n5']).fetchone(), m10.total, m10.falta],
             ['Socio', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n5']).fetchone(), m11.total, m11.falta],
             ['Filo', cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n1']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n2']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n3']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n4']).fetchone(), cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n5']).fetchone(), m12.total, m12.falta]]
    


tabela = CTkTable(app, row=13, column=8, values= value)
tabela.pack(padx=20, pady=20)




# Matemática
persiste_dados(m1, 1, 'Matemática')

# Biologia
persiste_dados(m2, 2, 'Biologia')

# Física
persiste_dados(m3, 3, 'Física')

# Química
persiste_dados(m4, 3, 'Química')

# Português
persiste_dados(m5, 5, 'Português')

# Literatura
persiste_dados(m6, 6, 'Literatura')

# Espanhol
persiste_dados(m7, 7, 'Espanhol')

# Inglês
persiste_dados(m8, 8, 'Inglês')

# História
persiste_dados(m9, 9, 'História')

# Geografia
persiste_dados(m10, 10, 'Geografia')

# Sociologia
persiste_dados(m11, 11, 'Sociologia')

# Filosofia
persiste_dados(m12, 12, 'Filosofia')


# Spinbox para a escolha da nota que será inserida
def select_spb2(self):
    global spinbox2
    global z
    spinbox2 = ctk.CTkOptionMenu(app, values= ['1ª', '2ª', '3ª', '4ª', '5ª'], width= 80, command= select, fg_color='#A020F0', button_color='#A020F0', button_hover_color='#9400D3',dropdown_hover_color='#A020F0')
    spinbox2.place(x=435, y=450)

# Menu Option para escolher a matéria 
def Inserir():
    global menu
    menu = ctk.CTkOptionMenu(app, values= ['Matemática', 'Biologia', 'Física', 'Química', 'Português', 'Literatura', 'Espanhol', 'Inglês', 'História', 'Geografia', 'Sociologia', 'Filosofia'], command= select_spb2, fg_color='#A020F0', button_color='#A020F0', button_hover_color='#9400D3',dropdown_hover_color='#A020F0')
    menu.place(x=281, y=450)


# Entrys e Botão Submit
def select(self):
    global btn_sbt
    global x
    global input_nota
    x = menu.get()
    if x == 'Matemática':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota mat')
        input_nota.place(x=325, y=490)
    if x == 'Biologia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota bio')
        input_nota.place(x=325, y=490)
    if x == 'Física':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota fis')
        input_nota.place(x=325, y=490)
    if x == 'Química':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota qui')
        input_nota.place(x=325, y=490)
    if x == 'Português':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota port')
        input_nota.place(x=325, y=490)
    if x == 'Literatura':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota lit')
        input_nota.place(x=325, y=490)
    if x == 'Espanhol':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota esp')
        input_nota.place(x=325, y=490)
    if x == 'Inglês':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota ing')
        input_nota.place(x=325, y=490)
    if x == 'História':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota hist')
        input_nota.place(x=325, y=490)
    if x == 'Geografia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota geo')
        input_nota.place(x=325, y=490)
    if x == 'Sociologia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota socio')
        input_nota.place(x=325, y=490)
    if x == 'Filosofia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota filo')
        input_nota.place(x=325, y=490)


    btn_sbt = ctk.CTkButton(app, text='enviar',  fg_color='#A020F0', hover_color='#9400D3',command=submit, width= 60,)
    btn_sbt.place(x=365, y=530)
    
# Lógica por trás do Insert das notas
def submit():
    z = spinbox2.get()
    if x == 'Matemática':
        if len(m1.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m1.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=1, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                    m1.notas = [nota[0] for nota in result_notas]
                    m1.total = sum(m1.notas)
                    tabela.insert(row=1, column=6, value=m1.total)
                    m1.falta = 7 - m1.total
                    if m1.falta <= 0:
                        m1.falta = 'Passou'
                    tabela.insert(row=1, column=7, value=m1.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m1.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=1, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                    m1.notas = [nota[0] for nota in result_notas]
                    m1.total = sum(m1.notas)
                    tabela.insert(row=1, column=6, value=m1.total)
                    m1.falta = 7 - m1.total
                    if m1.falta <= 0:
                        m1.falta = 'Passou'
                    tabela.insert(row=1, column=7, value=m1.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m1.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=1, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                    m1.notas = [nota[0] for nota in result_notas]
                    m1.total = sum(m1.notas)
                    tabela.insert(row=1, column=6, value=m1.total)
                    m1.falta = 7 - m1.total
                    if m1.falta <= 0:
                        m1.falta = 'Passou'
                    tabela.insert(row=1, column=7, value=m1.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m1.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=1, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                    m1.notas = [nota[0] for nota in result_notas]
                    m1.total = sum(m1.notas)
                    tabela.insert(row=1, column=6, value=m1.total)
                    m1.falta = 7 - m1.total
                    if m1.falta <= 0:
                        m1.falta = 'Passou'
                    tabela.insert(row=1, column=7, value=m1.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m1.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=1, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                    m1.notas = [nota[0] for nota in result_notas]
                    m1.total = sum(m1.notas)
                    tabela.insert(row=1, column=6, value=m1.total)
                    m1.falta = 7 - m1.total
                    if m1.falta <= 0:
                        m1.falta = 'Passou'
                    tabela.insert(row=1, column=7, value=m1.falta)


    elif x == 'Biologia':
        if len(m2.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m2.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=2, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                    m2.notas = [nota[0] for nota in result_notas]
                    m2.total = sum(m2.notas)
                    tabela.insert(row=2, column=6, value=m2.total)
                    m2.falta = 7 - m2.total
                    if m2.falta <= 0:
                        m2.falta = 'Passou'
                    tabela.insert(row=2, column=7, value=m2.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m2.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=2, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                    m2.notas = [nota[0] for nota in result_notas]
                    m2.total = sum(m2.notas)
                    tabela.insert(row=2, column=6, value=m2.total)
                    m2.falta = 7 - m2.total
                    if m2.falta <= 0:
                        m2.falta = 'Passou'
                    tabela.insert(row=2, column=7, value=m2.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m2.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=2, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                    m2.notas = [nota[0] for nota in result_notas]
                    m2.total = sum(m2.notas)
                    tabela.insert(row=2, column=6, value=m2.total)
                    m2.falta = 7 - m2.total
                    if m2.falta <= 0:
                        m2.falta = 'Passou'
                    tabela.insert(row=2, column=7, value=m2.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m2.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=2, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                    m2.notas = [nota[0] for nota in result_notas]
                    m2.total = sum(m2.notas)
                    tabela.insert(row=2, column=6, value=m2.total)
                    m2.falta = 7 - m2.total
                    if m2.falta <= 0:
                        m2.falta = 'Passou'
                    tabela.insert(row=2, column=7, value=m2.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m2.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=2, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                    m2.notas = [nota[0] for nota in result_notas]
                    m2.total = sum(m2.notas)
                    tabela.insert(row=2, column=6, value=m2.total)
                    m2.falta = 7 - m2.total
                    if m2.falta <= 0:
                        m2.falta = 'Passou'
                    tabela.insert(row=2, column=7, value=m2.falta)


    elif x == 'Física':
        if len(m3.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m3.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=3, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                    m3.notas = [nota[0] for nota in result_notas]
                    m3.total = sum(m3.notas)
                    tabela.insert(row=3, column=6, value=m3.total)
                    m3.falta = 7 - m3.total
                    if m3.falta <= 0:
                        m3.falta = 'Passou'
                    tabela.insert(row=3, column=7, value=m3.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m3.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=3, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                    m3.notas = [nota[0] for nota in result_notas]
                    m3.total = sum(m3.notas)
                    tabela.insert(row=3, column=6, value=m3.total)
                    m3.falta = 7 - m3.total
                    if m3.falta <= 0:
                        m3.falta = 'Passou'
                    tabela.insert(row=3, column=7, value=m3.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m3.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=3, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                    m3.notas = [nota[0] for nota in result_notas]
                    m3.total = sum(m3.notas)
                    tabela.insert(row=3, column=6, value=m3.total)
                    m3.falta = 7 - m3.total
                    if m3.falta <= 0:
                        m3.falta = 'Passou'
                    tabela.insert(row=3, column=7, value=m3.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m3.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=3, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                    m3.notas = [nota[0] for nota in result_notas]
                    m3.total = sum(m3.notas)
                    tabela.insert(row=3, column=6, value=m3.total)
                    m3.falta = 7 - m3.total
                    if m3.falta <= 0:
                        m3.falta = 'Passou'
                    tabela.insert(row=3, column=7, value=m3.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m3.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=3, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                    m3.notas = [nota[0] for nota in result_notas]
                    m3.total = sum(m3.notas)
                    tabela.insert(row=3, column=6, value=m3.total)
                    m3.falta = 7 - m3.total
                    if m3.falta <= 0:
                        m3.falta = 'Passou'
                    tabela.insert(row=3, column=7, value=m3.falta)


    elif x == 'Química':
        if len(m4.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m4.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=4, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                    m4.notas = [nota[0] for nota in result_notas]
                    m4.total = sum(m4.notas)
                    tabela.insert(row=4, column=6, value=m4.total)
                    m4.falta = 7 - m4.total
                    if m4.falta <= 0:
                        m4.falta = 'Passou'
                    tabela.insert(row=4, column=7, value=m4.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m4.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=4, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                    m4.notas = [nota[0] for nota in result_notas]
                    m4.total = sum(m4.notas)
                    tabela.insert(row=4, column=6, value=m4.total)
                    m4.falta = 7 - m4.total
                    if m4.falta <= 0:
                        m4.falta = 'Passou'
                    tabela.insert(row=4, column=7, value=m4.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m4.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=4, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                    m4.notas = [nota[0] for nota in result_notas]
                    m4.total = sum(m4.notas)
                    tabela.insert(row=4, column=6, value=m4.total)
                    m4.falta = 7 - m4.total
                    if m4.falta <= 0:
                        m4.falta = 'Passou'
                    tabela.insert(row=4, column=7, value=m4.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m4.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=4, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                    m4.notas = [nota[0] for nota in result_notas]
                    m4.total = sum(m4.notas)
                    tabela.insert(row=4, column=6, value=m4.total)
                    m4.falta = 7 - m4.total
                    if m4.falta <= 0:
                        m4.falta = 'Passou'
                    tabela.insert(row=4, column=7, value=m4.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m4.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=4, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                    m4.notas = [nota[0] for nota in result_notas]
                    m4.total = sum(m4.notas)
                    tabela.insert(row=4, column=6, value=m4.total)
                    m4.falta = 7 - m4.total
                    if m4.falta <= 0:
                        m4.falta = 'Passou'
                    tabela.insert(row=4, column=7, value=m4.falta)


    elif x == 'Português':
        if len(m5.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m5.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=5, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                    m5.notas = [nota[0] for nota in result_notas]
                    m5.total = sum(m5.notas)
                    tabela.insert(row=5, column=6, value=m5.total)
                    m5.falta = 7 - m5.total
                    if m5.falta <= 0:
                        m5.falta = 'Passou'
                    tabela.insert(row=5, column=7, value=m5.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m5.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=5, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                    m5.notas = [nota[0] for nota in result_notas]
                    m5.total = sum(m5.notas)
                    tabela.insert(row=5, column=6, value=m5.total)
                    m5.falta = 7 - m5.total
                    if m5.falta <= 0:
                        m5.falta = 'Passou'
                    tabela.insert(row=5, column=7, value=m5.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m5.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=5, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                    m5.notas = [nota[0] for nota in result_notas]
                    m5.total = sum(m5.notas)
                    tabela.insert(row=5, column=6, value=m5.total)
                    m5.falta = 7 - m5.total
                    if m5.falta <= 0:
                        m5.falta = 'Passou'
                    tabela.insert(row=5, column=7, value=m5.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m5.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=5, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                    m5.notas = [nota[0] for nota in result_notas]
                    m5.total = sum(m5.notas)
                    tabela.insert(row=5, column=6, value=m5.total)
                    m5.falta = 7 - m5.total
                    if m5.falta <= 0:
                        m5.falta = 'Passou'
                    tabela.insert(row=5, column=7, value=m5.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m5.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=5, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                    m5.notas = [nota[0] for nota in result_notas]
                    m5.total = sum(m5.notas)
                    tabela.insert(row=5, column=6, value=m5.total)
                    m5.falta = 7 - m5.total
                    if m5.falta <= 0:
                        m5.falta = 'Passou'
                    tabela.insert(row=5, column=7, value=m5.falta)


    elif x == 'Literatura':
        if len(m6.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m6.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=6, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                    m6.notas = [nota[0] for nota in result_notas]
                    m6.total = sum(m6.notas)
                    tabela.insert(row=6, column=6, value=m6.total)
                    m6.falta = 7 - m6.total
                    if m6.falta <= 0:
                        m6.falta = 'Passou'
                    tabela.insert(row=6, column=7, value=m6.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m6.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=6, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                    m6.notas = [nota[0] for nota in result_notas]
                    m6.total = sum(m6.notas)
                    tabela.insert(row=6, column=6, value=m6.total)
                    m6.falta = 7 - m6.total
                    if m6.falta <= 0:
                        m6.falta = 'Passou'
                    tabela.insert(row=6, column=7, value=m6.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m6.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=6, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                    m6.notas = [nota[0] for nota in result_notas]
                    m6.total = sum(m6.notas)
                    tabela.insert(row=6, column=6, value=m6.total)
                    m6.falta = 7 - m6.total
                    if m6.falta <= 0:
                        m6.falta = 'Passou'
                    tabela.insert(row=6, column=7, value=m6.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m6.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=6, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                    m6.notas = [nota[0] for nota in result_notas]
                    m6.total = sum(m6.notas)
                    tabela.insert(row=6, column=6, value=m6.total)
                    m6.falta = 7 - m6.total
                    if m6.falta <= 0:
                        m6.falta = 'Passou'
                    tabela.insert(row=6, column=7, value=m6.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m6.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=6, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                    m6.notas = [nota[0] for nota in result_notas]
                    m6.total = sum(m6.notas)
                    tabela.insert(row=6, column=6, value=m6.total)
                    m6.falta = 7 - m6.total
                    if m6.falta <= 0:
                        m6.falta = 'Passou'
                    tabela.insert(row=6, column=7, value=m6.falta)


    elif x == 'Espanhol':
        if len(m7.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m7.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=7, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                    m7.notas = [nota[0] for nota in result_notas]
                    m7.total = sum(m7.notas)
                    tabela.insert(row=7, column=6, value=m7.total)
                    m7.falta = 7 - m7.total
                    if m7.falta <= 0:
                        m7.falta = 'Passou'
                    tabela.insert(row=7, column=7, value=m7.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m7.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=7, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                    m7.notas = [nota[0] for nota in result_notas]
                    m7.total = sum(m7.notas)
                    tabela.insert(row=7, column=6, value=m7.total)
                    m7.falta = 7 - m7.total
                    if m7.falta <= 0:
                        m7.falta = 'Passou'
                    tabela.insert(row=7, column=7, value=m7.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m7.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=7, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                    m7.notas = [nota[0] for nota in result_notas]
                    m7.total = sum(m7.notas)
                    tabela.insert(row=7, column=6, value=m7.total)
                    m7.falta = 7 - m7.total
                    if m7.falta <= 0:
                        m7.falta = 'Passou'
                    tabela.insert(row=7, column=7, value=m7.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m7.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=7, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                    m7.notas = [nota[0] for nota in result_notas]
                    m7.total = sum(m7.notas)
                    tabela.insert(row=7, column=6, value=m7.total)
                    m7.falta = 7 - m7.total
                    if m7.falta <= 0:
                        m7.falta = 'Passou'
                    tabela.insert(row=7, column=7, value=m7.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m7.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=7, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                    m7.notas = [nota[0] for nota in result_notas]
                    m7.total = sum(m7.notas)
                    tabela.insert(row=7, column=6, value=m7.total)
                    m7.falta = 7 - m7.total
                    if m7.falta <= 0:
                        m7.falta = 'Passou'
                    tabela.insert(row=7, column=7, value=m7.falta)


    elif x == 'Inglês':
        if len(m8.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m8.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=8, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                    m8.notas = [nota[0] for nota in result_notas]
                    m8.total = sum(m8.notas)
                    tabela.insert(row=8, column=6, value=m8.total)
                    m8.falta = 7 - m8.total
                    if m8.falta <= 0:
                        m8.falta = 'Passou'
                    tabela.insert(row=8, column=7, value=m8.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m8.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=8, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                    m8.notas = [nota[0] for nota in result_notas]
                    m8.total = sum(m8.notas)
                    tabela.insert(row=8, column=6, value=m8.total)
                    m8.falta = 7 - m8.total
                    if m8.falta <= 0:
                        m8.falta = 'Passou'
                    tabela.insert(row=8, column=7, value=m8.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m8.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=8, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                    m8.notas = [nota[0] for nota in result_notas]
                    m8.total = sum(m8.notas)
                    tabela.insert(row=8, column=6, value=m8.total)
                    m8.falta = 7 - m8.total
                    if m8.falta <= 0:
                        m8.falta = 'Passou'
                    tabela.insert(row=8, column=7, value=m8.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m8.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=8, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                    m8.notas = [nota[0] for nota in result_notas]
                    m8.total = sum(m8.notas)
                    tabela.insert(row=8, column=6, value=m8.total)
                    m8.falta = 7 - m8.total
                    if m8.falta <= 0:
                        m8.falta = 'Passou'
                    tabela.insert(row=8, column=7, value=m8.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m8.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=8, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                    m8.notas = [nota[0] for nota in result_notas]
                    m8.total = sum(m8.notas)
                    tabela.insert(row=8, column=6, value=m8.total)
                    m8.falta = 7 - m8.total
                    if m8.falta <= 0:
                        m8.falta = 'Passou'
                    tabela.insert(row=8, column=7, value=m8.falta)


    elif x == 'História':
        if len(m9.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m9.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=9, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                    m9.notas = [nota[0] for nota in result_notas]
                    m9.total = sum(m9.notas)
                    tabela.insert(row=9, column=6, value=m9.total)
                    m9.falta = 7 - m9.total
                    if m9.falta <= 0:
                        m9.falta = 'Passou'
                    tabela.insert(row=9, column=7, value=m9.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m9.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=9, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                    m9.notas = [nota[0] for nota in result_notas]
                    m9.total = sum(m9.notas)
                    tabela.insert(row=9, column=6, value=m9.total)
                    m9.falta = 7 - m9.total
                    if m9.falta <= 0:
                        m9.falta = 'Passou'
                    tabela.insert(row=9, column=7, value=m9.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m9.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=9, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                    m9.notas = [nota[0] for nota in result_notas]
                    m9.total = sum(m9.notas)
                    tabela.insert(row=9, column=6, value=m9.total)
                    m9.falta = 7 - m9.total
                    if m9.falta <= 0:
                        m9.falta = 'Passou'
                    tabela.insert(row=9, column=7, value=m9.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m9.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=9, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                    m9.notas = [nota[0] for nota in result_notas]
                    m9.total = sum(m9.notas)
                    tabela.insert(row=9, column=6, value=m9.total)
                    m9.falta = 7 - m9.total
                    if m9.falta <= 0:
                        m9.falta = 'Passou'
                    tabela.insert(row=9, column=7, value=m9.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m9.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=9, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                    m9.notas = [nota[0] for nota in result_notas]
                    m9.total = sum(m9.notas)
                    tabela.insert(row=9, column=6, value=m9.total)
                    m9.falta = 7 - m9.total
                    if m9.falta <= 0:
                        m9.falta = 'Passou'
                    tabela.insert(row=9, column=7, value=m9.falta)


    elif x == 'Geografia':
        if len(m10.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m10.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=10, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                    m10.notas = [nota[0] for nota in result_notas]
                    m10.total = sum(m10.notas)
                    tabela.insert(row=10, column=6, value=m10.total)
                    m10.falta = 7 - m10.total
                    if m10.falta <= 0:
                        m10.falta = 'Passou'
                    tabela.insert(row=10, column=7, value=m10.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m10.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=10, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                    m10.notas = [nota[0] for nota in result_notas]
                    m10.total = sum(m10.notas)
                    tabela.insert(row=10, column=6, value=m10.total)
                    m10.falta = 7 - m10.total
                    if m10.falta <= 0:
                        m10.falta = 'Passou'
                    tabela.insert(row=10, column=7, value=m10.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m10.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=10, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                    m10.notas = [nota[0] for nota in result_notas]
                    m10.total = sum(m10.notas)
                    tabela.insert(row=10, column=6, value=m10.total)
                    m10.falta = 7 - m10.total
                    if m10.falta <= 0:
                        m10.falta = 'Passou'
                    tabela.insert(row=10, column=7, value=m10.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m10.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=10, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                    m10.notas = [nota[0] for nota in result_notas]
                    m10.total = sum(m10.notas)
                    tabela.insert(row=10, column=6, value=m10.total)
                    m10.falta = 7 - m10.total
                    if m10.falta <= 0:
                        m10.falta = 'Passou'
                    tabela.insert(row=10, column=7, value=m10.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m10.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=10, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                    m10.notas = [nota[0] for nota in result_notas]
                    m10.total = sum(m10.notas)
                    tabela.insert(row=10, column=6, value=m10.total)
                    m10.falta = 7 - m10.total
                    if m10.falta <= 0:
                        m10.falta = 'Passou'
                    tabela.insert(row=10, column=7, value=m10.falta)


    elif x == 'Sociologia':
        if len(m11.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m11.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=11, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                    m11.notas = [nota[0] for nota in result_notas]
                    m11.total = sum(m11.notas)
                    tabela.insert(row=11, column=6, value=m11.total)
                    m11.falta = 7 - m11.total
                    if m11.falta <= 0:
                        m11.falta = 'Passou'
                    tabela.insert(row=11, column=7, value=m11.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m11.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=11, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                    m11.notas = [nota[0] for nota in result_notas]
                    m11.total = sum(m11.notas)
                    tabela.insert(row=11, column=6, value=m11.total)
                    m11.falta = 7 - m11.total
                    if m11.falta <= 0:
                        m11.falta = 'Passou'
                    tabela.insert(row=11, column=7, value=m11.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m11.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=11, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                    m11.notas = [nota[0] for nota in result_notas]
                    m11.total = sum(m11.notas)
                    tabela.insert(row=11, column=6, value=m11.total)
                    m11.falta = 7 - m11.total
                    if m11.falta <= 0:
                        m11.falta = 'Passou'
                    tabela.insert(row=11, column=7, value=m11.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m11.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=11, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                    m11.notas = [nota[0] for nota in result_notas]
                    m11.total = sum(m11.notas)
                    tabela.insert(row=11, column=6, value=m11.total)
                    m11.falta = 7 - m11.total
                    if m11.falta <= 0:
                        m11.falta = 'Passou'
                    tabela.insert(row=11, column=7, value=m11.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m11.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=11, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                    m11.notas = [nota[0] for nota in result_notas]
                    m11.total = sum(m11.notas)
                    tabela.insert(row=11, column=6, value=m11.total)
                    m11.falta = 7 - m11.total
                    if m11.falta <= 0:
                        m11.falta = 'Passou'
                    tabela.insert(row=11, column=7, value=m11.falta)


    elif x == 'Filosofia':
        if len(m12.notas) <= 4:
            if z == '1ª':
                num_nota = 'n1'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n1']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m12.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=12, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n1']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                    m12.notas = [nota[0] for nota in result_notas]
                    m12.total = sum(m12.notas)
                    tabela.insert(row=12, column=6, value=m12.total)
                    m12.falta = 7 - m12.total
                    if m12.falta <= 0:
                        m12.falta = 'Passou'
                    tabela.insert(row=12, column=7, value=m12.falta)
            if z == '2ª':
                num_nota = 'n2'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n2']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m12.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=12, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n2']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                    m12.notas = [nota[0] for nota in result_notas]
                    m12.total = sum(m12.notas)
                    tabela.insert(row=12, column=6, value=m12.total)
                    m12.falta = 7 - m12.total
                    if m12.falta <= 0:
                        m12.falta = 'Passou'
                    tabela.insert(row=12, column=7, value=m12.falta)
            if z == '3ª':
                num_nota = 'n3'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n3']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m12.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=12, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n3']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                    m12.notas = [nota[0] for nota in result_notas]
                    m12.total = sum(m12.notas)
                    tabela.insert(row=12, column=6, value=m12.total)
                    m12.falta = 7 - m12.total
                    if m12.falta <= 0:
                        m12.falta = 'Passou'
                    tabela.insert(row=12, column=7, value=m12.falta)
            if z == '4ª':
                num_nota = 'n4'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n4']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m12.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=12, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n4']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                    m12.notas = [nota[0] for nota in result_notas]
                    m12.total = sum(m12.notas)
                    tabela.insert(row=12, column=6, value=m12.total)
                    m12.falta = 7 - m12.total
                    if m12.falta <= 0:
                        m12.falta = 'Passou'
                    tabela.insert(row=12, column=7, value=m12.falta)
            if z == '5ª':
                num_nota = 'n5'
                notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n5']).fetchone()
                if notasref is None:
                    query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES
                    (?, ?, ?)'''
                    tupla_inserir_dados = (m12.nome, num_nota, input_nota.get())
                    cursor.execute(query_inserir_data, tupla_inserir_dados)
                    con.commit()
                    tabela.insert(row=12, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n5']).fetchone())
                    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                    m12.notas = [nota[0] for nota in result_notas]
                    m12.total = sum(m12.notas)
                    tabela.insert(row=12, column=6, value=m12.total)
                    m12.falta = 7 - m12.total
                    if m12.falta <= 0:
                        m12.falta = 'Passou'
                    tabela.insert(row=12, column=7, value=m12.falta)


    # Resetando os botões (Despoluindo a tela)
    btn_sbt.destroy()
    input_nota.destroy()
    menu.destroy()
    spinbox2.destroy()
    

btn_inserir = ctk.CTkButton(app, text='Inserir', command= Inserir, width=100, fg_color='#A020F0', hover_color='#9400D3')
btn_inserir.place(x= 281, y=410)


# Spinbox para a escolha da nota que será editada
def select_spb(self):
    global spinbox
    global editz
    spinbox = ctk.CTkOptionMenu(app, values= ['1ª', '2ª', '3ª', '4ª', '5ª'], width= 80, command= select_edit, fg_color='#A020F0', button_color='#A020F0', button_hover_color='#9400D3',dropdown_hover_color='#A020F0')
    spinbox.place(x=435, y=450)

# Entrys e Botão Edit
def select_edit(self):
    global btn_att
    global input_nota_edit
    global y
    y = menu_edit.get()
    if y == 'Matemática':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota mat')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Biologia':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota bio')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Física':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota fis')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Química':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota qui')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Português':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota port')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Literatura':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota lit')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Espanhol':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota esp')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Inglês':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota ing')
        input_nota_edit.place(x=325, y=490)
    elif y == 'História':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota hist')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Geografia':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota geo')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Sociologia':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota socio')
        input_nota_edit.place(x=325, y=490)
    elif y == 'Filosofia':
        input_nota_edit = ctk.CTkEntry(app, placeholder_text='Nota filo')
        input_nota_edit.place(x=325, y=490)

    btn_att = ctk.CTkButton(app, text='atualizar', command=att, width= 60, fg_color='#A020F0', hover_color='#9400D3')
    btn_att.place(x=365, y=530)

# Lógica por trás do Edit das notas
def att():
    editz = spinbox.get()
    if y == 'Matemática':
        if len(m1.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=1, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                m1.notas = [nota[0] for nota in result_notas]
                m1.total = sum(m1.notas)
                tabela.insert(row=1, column=6, value=m1.total)
                m1.falta = 7 - m1.total
                if m1.falta <= 0:
                    m1.falta = 'Passou'
                tabela.insert(row=1, column=7, value=m1.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=1, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                m1.notas = [nota[0] for nota in result_notas]
                m1.total = sum(m1.notas)
                tabela.insert(row=1, column=6, value=m1.total)
                m1.falta = 7 - m1.total
                if m1.falta <= 0:
                    m1.falta = 'Passou'
                tabela.insert(row=1, column=7, value=m1.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=1, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                m1.notas = [nota[0] for nota in result_notas]
                m1.total = sum(m1.notas)
                tabela.insert(row=1, column=6, value=m1.total)
                m1.falta = 7 - m1.total
                if m1.falta <= 0:
                    m1.falta = 'Passou'
                tabela.insert(row=1, column=7, value=m1.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=1, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                m1.notas = [nota[0] for nota in result_notas]
                m1.total = sum(m1.notas)
                tabela.insert(row=1, column=6, value=m1.total)
                m1.falta = 7 - m1.total
                if m1.falta <= 0:
                    m1.falta = 'Passou'
                tabela.insert(row=1, column=7, value=m1.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=1, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Matemática', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Matemática']).fetchall()
                m1.notas = [nota[0] for nota in result_notas]
                m1.total = sum(m1.notas)
                tabela.insert(row=1, column=6, value=m1.total)
                m1.falta = 7 - m1.total
                if m1.falta <= 0:
                    m1.falta = 'Passou'
                tabela.insert(row=1, column=7, value=m1.falta)


    if y == 'Biologia':
        if len(m2.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=2, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                m2.notas = [nota[0] for nota in result_notas]
                m2.total = sum(m2.notas)
                tabela.insert(row=2, column=6, value=m2.total)
                m2.falta = 7 - m2.total
                if m2.falta <= 0:
                    m2.falta = 'Passou'
                tabela.insert(row=2, column=7, value=m2.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=2, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                m2.notas = [nota[0] for nota in result_notas]
                m2.total = sum(m2.notas)
                tabela.insert(row=2, column=6, value=m2.total)
                m2.falta = 7 - m2.total
                if m2.falta <= 0:
                    m2.falta = 'Passou'
                tabela.insert(row=2, column=7, value=m2.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=2, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                m2.notas = [nota[0] for nota in result_notas]
                m2.total = sum(m2.notas)
                tabela.insert(row=2, column=6, value=m2.total)
                m2.falta = 7 - m2.total
                if m2.falta <= 0:
                    m2.falta = 'Passou'
                tabela.insert(row=2, column=7, value=m2.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=2, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                m2.notas = [nota[0] for nota in result_notas]
                m2.total = sum(m2.notas)
                tabela.insert(row=2, column=6, value=m2.total)
                m2.falta = 7 - m2.total
                if m2.falta <= 0:
                    m2.falta = 'Passou'
                tabela.insert(row=2, column=7, value=m2.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=2, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Biologia', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Biologia']).fetchall()
                m2.notas = [nota[0] for nota in result_notas]
                m2.total = sum(m2.notas)
                tabela.insert(row=2, column=6, value=m2.total)
                m2.falta = 7 - m2.total
                if m2.falta <= 0:
                    m2.falta = 'Passou'
                tabela.insert(row=2, column=7, value=m2.falta)


    if y == 'Física':
        if len(m3.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=3, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                m3.notas = [nota[0] for nota in result_notas]
                m3.total = sum(m3.notas)
                tabela.insert(row=3, column=6, value=m3.total)
                m3.falta = 7 - m3.total
                if m3.falta <= 0:
                    m3.falta = 'Passou'
                tabela.insert(row=3, column=7, value=m3.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=3, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                m3.notas = [nota[0] for nota in result_notas]
                m3.total = sum(m3.notas)
                tabela.insert(row=3, column=6, value=m3.total)
                m3.falta = 7 - m3.total
                if m3.falta <= 0:
                    m3.falta = 'Passou'
                tabela.insert(row=3, column=7, value=m3.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=3, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                m3.notas = [nota[0] for nota in result_notas]
                m3.total = sum(m3.notas)
                tabela.insert(row=3, column=6, value=m3.total)
                m3.falta = 7 - m3.total
                if m3.falta <= 0:
                    m3.falta = 'Passou'
                tabela.insert(row=3, column=7, value=m3.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=3, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                m3.notas = [nota[0] for nota in result_notas]
                m3.total = sum(m3.notas)
                tabela.insert(row=3, column=6, value=m3.total)
                m3.falta = 7 - m3.total
                if m3.falta <= 0:
                    m3.falta = 'Passou'
                tabela.insert(row=3, column=7, value=m3.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=3, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Física', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Física']).fetchall()
                m3.notas = [nota[0] for nota in result_notas]
                m3.total = sum(m3.notas)
                tabela.insert(row=3, column=6, value=m3.total)
                m3.falta = 7 - m3.total
                if m3.falta <= 0:
                    m3.falta = 'Passou'
                tabela.insert(row=3, column=7, value=m3.falta)


    if y == 'Química':
        if len(m4.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=4, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                m4.notas = [nota[0] for nota in result_notas]
                m4.total = sum(m4.notas)
                tabela.insert(row=4, column=6, value=m4.total)
                m4.falta = 7 - m4.total
                if m4.falta <= 0:
                    m4.falta = 'Passou'
                tabela.insert(row=4, column=7, value=m4.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=4, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                m4.notas = [nota[0] for nota in result_notas]
                m4.total = sum(m4.notas)
                tabela.insert(row=4, column=6, value=m4.total)
                m4.falta = 7 - m4.total
                if m4.falta <= 0:
                    m4.falta = 'Passou'
                tabela.insert(row=4, column=7, value=m4.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=4, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                m4.notas = [nota[0] for nota in result_notas]
                m4.total = sum(m4.notas)
                tabela.insert(row=4, column=6, value=m4.total)
                m4.falta = 7 - m4.total
                if m4.falta <= 0:
                    m4.falta = 'Passou'
                tabela.insert(row=4, column=7, value=m4.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=4, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                m4.notas = [nota[0] for nota in result_notas]
                m4.total = sum(m4.notas)
                tabela.insert(row=4, column=6, value=m4.total)
                m4.falta = 7 - m4.total
                if m4.falta <= 0:
                    m4.falta = 'Passou'
                tabela.insert(row=4, column=7, value=m4.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=4, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Química', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Química']).fetchall()
                m4.notas = [nota[0] for nota in result_notas]
                m4.total = sum(m4.notas)
                tabela.insert(row=4, column=6, value=m4.total)
                m4.falta = 7 - m4.total
                if m4.falta <= 0:
                    m4.falta = 'Passou'
                tabela.insert(row=4, column=7, value=m4.falta)


    if y == 'Português':
        if len(m5.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=5, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                m5.notas = [nota[0] for nota in result_notas]
                m5.total = sum(m5.notas)
                tabela.insert(row=5, column=6, value=m5.total)
                m5.falta = 7 - m5.total
                if m5.falta <= 0:
                    m5.falta = 'Passou'
                tabela.insert(row=5, column=7, value=m5.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=5, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                m5.notas = [nota[0] for nota in result_notas]
                m5.total = sum(m5.notas)
                tabela.insert(row=5, column=6, value=m5.total)
                m5.falta = 7 - m5.total
                if m5.falta <= 0:
                    m5.falta = 'Passou'
                tabela.insert(row=5, column=7, value=m5.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=5, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                m5.notas = [nota[0] for nota in result_notas]
                m5.total = sum(m5.notas)
                tabela.insert(row=5, column=6, value=m5.total)
                m5.falta = 7 - m5.total
                if m5.falta <= 0:
                    m5.falta = 'Passou'
                tabela.insert(row=5, column=7, value=m5.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=5, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                m5.notas = [nota[0] for nota in result_notas]
                m5.total = sum(m5.notas)
                tabela.insert(row=5, column=6, value=m5.total)
                m5.falta = 7 - m5.total
                if m5.falta <= 0:
                    m5.falta = 'Passou'
                tabela.insert(row=5, column=7, value=m5.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=5, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Português', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Português']).fetchall()
                m5.notas = [nota[0] for nota in result_notas]
                m5.total = sum(m5.notas)
                tabela.insert(row=5, column=6, value=m5.total)
                m5.falta = 7 - m5.total
                if m5.falta <= 0:
                    m5.falta = 'Passou'
                tabela.insert(row=5, column=7, value=m5.falta)


    if y == 'Literatura':
        if len(m6.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=6, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                m6.notas = [nota[0] for nota in result_notas]
                m6.total = sum(m6.notas)
                tabela.insert(row=6, column=6, value=m6.total)
                m6.falta = 7 - m6.total
                if m6.falta <= 0:
                    m6.falta = 'Passou'
                tabela.insert(row=6, column=7, value=m6.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=6, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                m6.notas = [nota[0] for nota in result_notas]
                m6.total = sum(m6.notas)
                tabela.insert(row=6, column=6, value=m6.total)
                m6.falta = 7 - m6.total
                if m6.falta <= 0:
                    m6.falta = 'Passou'
                tabela.insert(row=6, column=7, value=m6.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=6, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                m6.notas = [nota[0] for nota in result_notas]
                m6.total = sum(m6.notas)
                tabela.insert(row=6, column=6, value=m6.total)
                m6.falta = 7 - m6.total
                if m6.falta <= 0:
                    m6.falta = 'Passou'
                tabela.insert(row=6, column=7, value=m6.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=6, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                m6.notas = [nota[0] for nota in result_notas]
                m6.total = sum(m6.notas)
                tabela.insert(row=6, column=6, value=m6.total)
                m6.falta = 7 - m6.total
                if m6.falta <= 0:
                    m6.falta = 'Passou'
                tabela.insert(row=6, column=7, value=m6.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=6, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Literatura', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Literatura']).fetchall()
                m6.notas = [nota[0] for nota in result_notas]
                m6.total = sum(m6.notas)
                tabela.insert(row=6, column=6, value=m6.total)
                m6.falta = 7 - m6.total
                if m6.falta <= 0:
                    m6.falta = 'Passou'
                tabela.insert(row=6, column=7, value=m6.falta)


    if y == 'Espanhol':
        if len(m7.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=7, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                m7.notas = [nota[0] for nota in result_notas]
                m7.total = sum(m7.notas)
                tabela.insert(row=7, column=6, value=m7.total)
                m7.falta = 7 - m7.total
                if m7.falta <= 0:
                    m7.falta = 'Passou'
                tabela.insert(row=7, column=7, value=m7.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=7, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                m7.notas = [nota[0] for nota in result_notas]
                m7.total = sum(m7.notas)
                tabela.insert(row=7, column=6, value=m7.total)
                m7.falta = 7 - m7.total
                if m7.falta <= 0:
                    m7.falta = 'Passou'
                tabela.insert(row=7, column=7, value=m7.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=7, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                m7.notas = [nota[0] for nota in result_notas]
                m7.total = sum(m7.notas)
                tabela.insert(row=7, column=6, value=m7.total)
                m7.falta = 7 - m7.total
                if m7.falta <= 0:
                    m7.falta = 'Passou'
                tabela.insert(row=7, column=7, value=m7.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=7, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                m7.notas = [nota[0] for nota in result_notas]
                m7.total = sum(m7.notas)
                tabela.insert(row=7, column=6, value=m7.total)
                m7.falta = 7 - m7.total
                if m7.falta <= 0:
                    m7.falta = 'Passou'
                tabela.insert(row=7, column=7, value=m7.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=7, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Espanhol', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Espanhol']).fetchall()
                m7.notas = [nota[0] for nota in result_notas]
                m7.total = sum(m7.notas)
                tabela.insert(row=7, column=6, value=m7.total)
                m7.falta = 7 - m7.total
                if m7.falta <= 0:
                    m7.falta = 'Passou'
                tabela.insert(row=7, column=7, value=m7.falta)


    if y == 'Inglês':
        if len(m8.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=8, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                m8.notas = [nota[0] for nota in result_notas]
                m8.total = sum(m8.notas)
                tabela.insert(row=8, column=6, value=m8.total)
                m8.falta = 7 - m8.total
                if m8.falta <= 0:
                    m8.falta = 'Passou'
                tabela.insert(row=8, column=7, value=m8.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=8, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                m8.notas = [nota[0] for nota in result_notas]
                m8.total = sum(m8.notas)
                tabela.insert(row=8, column=6, value=m8.total)
                m8.falta = 7 - m8.total
                if m8.falta <= 0:
                    m8.falta = 'Passou'
                tabela.insert(row=8, column=7, value=m8.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=8, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                m8.notas = [nota[0] for nota in result_notas]
                m8.total = sum(m8.notas)
                tabela.insert(row=8, column=6, value=m8.total)
                m8.falta = 7 - m8.total
                if m8.falta <= 0:
                    m8.falta = 'Passou'
                tabela.insert(row=8, column=7, value=m8.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=8, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                m8.notas = [nota[0] for nota in result_notas]
                m8.total = sum(m8.notas)
                tabela.insert(row=8, column=6, value=m8.total)
                m8.falta = 7 - m8.total
                if m8.falta <= 0:
                    m8.falta = 'Passou'
                tabela.insert(row=8, column=7, value=m8.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=8, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Inglês', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Inglês']).fetchall()
                m8.notas = [nota[0] for nota in result_notas]
                m8.total = sum(m8.notas)
                tabela.insert(row=8, column=6, value=m8.total)
                m8.falta = 7 - m8.total
                if m8.falta <= 0:
                    m8.falta = 'Passou'
                tabela.insert(row=8, column=7, value=m8.falta)


    if y == 'História':
        if len(m9.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=9, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                m9.notas = [nota[0] for nota in result_notas]
                m9.total = sum(m9.notas)
                tabela.insert(row=9, column=6, value=m9.total)
                m9.falta = 7 - m9.total
                if m9.falta <= 0:
                    m9.falta = 'Passou'
                tabela.insert(row=9, column=7, value=m9.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=9, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                m9.notas = [nota[0] for nota in result_notas]
                m9.total = sum(m9.notas)
                tabela.insert(row=9, column=6, value=m9.total)
                m9.falta = 7 - m9.total
                if m9.falta <= 0:
                    m9.falta = 'Passou'
                tabela.insert(row=9, column=7, value=m9.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=9, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                m9.notas = [nota[0] for nota in result_notas]
                m9.total = sum(m9.notas)
                tabela.insert(row=9, column=6, value=m9.total)
                m9.falta = 7 - m9.total
                if m9.falta <= 0:
                    m9.falta = 'Passou'
                tabela.insert(row=9, column=7, value=m9.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=9, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                m9.notas = [nota[0] for nota in result_notas]
                m9.total = sum(m9.notas)
                tabela.insert(row=9, column=6, value=m9.total)
                m9.falta = 7 - m9.total
                if m9.falta <= 0:
                    m9.falta = 'Passou'
                tabela.insert(row=9, column=7, value=m9.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=9, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['História', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['História']).fetchall()
                m9.notas = [nota[0] for nota in result_notas]
                m9.total = sum(m9.notas)
                tabela.insert(row=9, column=6, value=m9.total)
                m9.falta = 7 - m9.total
                if m9.falta <= 0:
                    m9.falta = 'Passou'
                tabela.insert(row=9, column=7, value=m9.falta)


    if y == 'Geografia':
        if len(m10.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=10, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                m10.notas = [nota[0] for nota in result_notas]
                m10.total = sum(m10.notas)
                tabela.insert(row=10, column=6, value=m10.total)
                m10.falta = 7 - m10.total
                if m10.falta <= 0:
                    m10.falta = 'Passou'
                tabela.insert(row=10, column=7, value=m10.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=10, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                m10.notas = [nota[0] for nota in result_notas]
                m10.total = sum(m10.notas)
                tabela.insert(row=10, column=6, value=m10.total)
                m10.falta = 7 - m10.total
                if m10.falta <= 0:
                    m10.falta = 'Passou'
                tabela.insert(row=10, column=7, value=m10.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=10, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                m10.notas = [nota[0] for nota in result_notas]
                m10.total = sum(m10.notas)
                tabela.insert(row=10, column=6, value=m10.total)
                m10.falta = 7 - m10.total
                if m10.falta <= 0:
                    m10.falta = 'Passou'
                tabela.insert(row=10, column=7, value=m10.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=10, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                m10.notas = [nota[0] for nota in result_notas]
                m10.total = sum(m10.notas)
                tabela.insert(row=10, column=6, value=m10.total)
                m10.falta = 7 - m10.total
                if m10.falta <= 0:
                    m10.falta = 'Passou'
                tabela.insert(row=10, column=7, value=m10.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=10, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Geografia', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Geografia']).fetchall()
                m10.notas = [nota[0] for nota in result_notas]
                m10.total = sum(m10.notas)
                tabela.insert(row=10, column=6, value=m10.total)
                m10.falta = 7 - m10.total
                if m10.falta <= 0:
                    m10.falta = 'Passou'
                tabela.insert(row=10, column=7, value=m10.falta)


    if y == 'Sociologia':
        if len(m11.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=11, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                m11.notas = [nota[0] for nota in result_notas]
                m11.total = sum(m11.notas)
                tabela.insert(row=11, column=6, value=m11.total)
                m11.falta = 7 - m11.total
                if m11.falta <= 0:
                    m11.falta = 'Passou'
                tabela.insert(row=11, column=7, value=m11.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=11, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                m11.notas = [nota[0] for nota in result_notas]
                m11.total = sum(m11.notas)
                tabela.insert(row=11, column=6, value=m11.total)
                m11.falta = 7 - m11.total
                if m11.falta <= 0:
                    m11.falta = 'Passou'
                tabela.insert(row=11, column=7, value=m11.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=11, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                m11.notas = [nota[0] for nota in result_notas]
                m11.total = sum(m11.notas)
                tabela.insert(row=11, column=6, value=m11.total)
                m11.falta = 7 - m11.total
                if m11.falta <= 0:
                    m11.falta = 'Passou'
                tabela.insert(row=11, column=7, value=m11.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=11, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                m11.notas = [nota[0] for nota in result_notas]
                m11.total = sum(m11.notas)
                tabela.insert(row=11, column=6, value=m11.total)
                m11.falta = 7 - m11.total
                if m11.falta <= 0:
                    m11.falta = 'Passou'
                tabela.insert(row=11, column=7, value=m11.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=11, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Sociologia', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Sociologia']).fetchall()
                m11.notas = [nota[0] for nota in result_notas]
                m11.total = sum(m11.notas)
                tabela.insert(row=11, column=6, value=m11.total)
                m11.falta = 7 - m11.total
                if m11.falta <= 0:
                    m11.falta = 'Passou'
                tabela.insert(row=11, column=7, value=m11.falta)


    if y == 'Filosofia':
        if len(m12.notas) <= 5:
            if editz == '1ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n1' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=12, column=1, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n1']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                m12.notas = [nota[0] for nota in result_notas]
                m12.total = sum(m12.notas)
                tabela.insert(row=12, column=6, value=m12.total)
                m12.falta = 7 - m12.total
                if m12.falta <= 0:
                    m12.falta = 'Passou'
                tabela.insert(row=12, column=7, value=m12.falta)
            elif editz == '2ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n2' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=12, column=2, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n2']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                m12.notas = [nota[0] for nota in result_notas]
                m12.total = sum(m12.notas)
                tabela.insert(row=12, column=6, value=m12.total)
                m12.falta = 7 - m12.total
                if m12.falta <= 0:
                    m12.falta = 'Passou'
                tabela.insert(row=12, column=7, value=m12.falta)
            elif editz == '3ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n3' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=12, column=3, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n3']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                m12.notas = [nota[0] for nota in result_notas]
                m12.total = sum(m12.notas)
                tabela.insert(row=12, column=6, value=m12.total)
                m12.falta = 7 - m12.total
                if m12.falta <= 0:
                    m12.falta = 'Passou'
                tabela.insert(row=12, column=7, value=m12.falta)
            elif editz == '4ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n4' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=12, column=4, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n4']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                m12.notas = [nota[0] for nota in result_notas]
                m12.total = sum(m12.notas)
                tabela.insert(row=12, column=6, value=m12.total)
                m12.falta = 7 - m12.total
                if m12.falta <= 0:
                    m12.falta = 'Passou'
                tabela.insert(row=12, column=7, value=m12.falta)
            elif editz == '5ª':
                query_atualizar_dados = ('''UPDATE boletim
                                SET nota = ?
                               WHERE notaref = 'n5' ''')
                tupla_atualizar_dados = (input_nota_edit.get(),)
                cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
                con.commit()
                tabela.insert(row=12, column=5, value= cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", ['Filosofia', 'n5']).fetchone())
                result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", ['Filosofia']).fetchall()
                m12.notas = [nota[0] for nota in result_notas]
                m12.total = sum(m12.notas)
                tabela.insert(row=12, column=6, value=m12.total)
                m12.falta = 7 - m12.total
                if m12.falta <= 0:
                    m12.falta = 'Passou'
                tabela.insert(row=12, column=7, value=m12.falta)


    # Resetando os botões
    menu_edit.destroy()
    spinbox.destroy()
    input_nota_edit.destroy()
    btn_att.destroy()

# Menu Option para escolher a matéria 
def Editar():
    global menu_edit
    menu_edit = ctk.CTkOptionMenu(app, values= ['Matemática', 'Biologia', 'Física', 'Química', 'Português', 'Literatura', 'Espanhol', 'Inglês', 'História', 'Geografia', 'Sociologia', 'Filosofia'], command=select_spb, fg_color='#A020F0', button_color='#A020F0', button_hover_color='#9400D3',dropdown_hover_color='#A020F0')
    menu_edit.place(x=281, y=450)

btn_editar = ctk.CTkButton(app, text='Editar', command= Editar, width=100, fg_color='#A020F0', hover_color='#9400D3')
btn_editar.place(x=417, y=410)


app.mainloop()