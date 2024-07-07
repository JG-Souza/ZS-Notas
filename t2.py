import customtkinter as ctk
from pathlib import Path
from tinydb import TinyDB
from CTkTable import *


app = ctk.CTk()
ctk.set_default_color_theme('green')
app.geometry('800x800')
app.title('Meu App')


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

def select(self):
    global x
    global input_nota
    x = menu.get()
    if x == 'Matemática':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota mat')
        input_nota.place(x=15, y=50)
    if x == 'Biologia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota bio')
        input_nota.place(x=15, y=50)
    if x == 'Física':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota fis')
        input_nota.place(x=15, y=50)
    if x == 'Química':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota qui')
        input_nota.place(x=15, y=50)
    if x == 'Português':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota port')
        input_nota.place(x=15, y=50)
    if x == 'Literatura':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota lit')
        input_nota.place(x=15, y=50)
    if x == 'Espanhol':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota esp')
        input_nota.place(x=15, y=50)
    if x == 'Inglês':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota ing')
        input_nota.place(x=15, y=50)
    if x == 'História':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota hist')
        input_nota.place(x=15, y=50)
    if x == 'Geografia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota geo')
        input_nota.place(x=15, y=50)
    if x == 'Sociologia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota socio')
        input_nota.place(x=15, y=50)
    if x == 'Filosofia':
        input_nota = ctk.CTkEntry(app, placeholder_text='Nota filo')
        input_nota.place(x=15, y=50)


    btn = ctk.CTkButton(app, text='submit', command=submit, width= 60)
    btn.place(x=190, y=50)
    

def submit():
    if x == 'Matemática':
        m1.notas.append(float(input_nota.get()))
        m1.total = sum(m1.notas)
        m1.falta = 7 - m1.total
        if m1.falta <= 0:
            m1.falta = 'Passou'
    if x == 'Biologia':
        m2.notas.append(float(input_nota.get()))
        m2.total = sum(m2.notas)
        m2.falta = 7 - m2.total
        if m2.falta <= 0:
            m2.falta = 'Passou'
    if x == 'Física':
        m3.notas.append(float(input_nota.get()))
        m3.total = sum(m3.notas)
        m3.falta = 7 - m3.total
        if m3.falta <= 0:
            m3.falta = 'Passou'
    if x == 'Química':
        m4.notas.append(float(input_nota.get()))
        m4.total = sum(m4.notas)
        m4.falta = 7 - m4.total
        if m4.falta <= 0:
            m4.falta = 'Passou'
    if x == 'Português':
        m5.notas.append(float(input_nota.get()))
        m5.total = sum(m5.notas)
        m5.falta = 7 - m5.total
        if m3.falta <= 0:
            m5.falta = 'Passou'
    if x == 'Literatura':
        m6.notas.append(float(input_nota.get()))
        m6.total = sum(m6.notas)
        m6.falta = 7 - m6.total
        if m6.falta <= 0:
            m6.falta = 'Passou'
    if x == 'Espanhol':
        m7.notas.append(float(input_nota.get()))
        m7.total = sum(m7.notas)
        m7.falta = 7 - m7.total
        if m7.falta <= 0:
            m7.falta = 'Passou'
    if x == 'Inglês':
        m8.notas.append(float(input_nota.get()))
        m8.total = sum(m8.notas)
        m8.falta = 7 - m8.total
        if m8.falta <= 0:
            m8.falta = 'Passou'
    if x == 'História':
        m9.notas.append(float(input_nota.get()))
        m9.total = sum(m9.notas)
        m9.falta = 7 - m9.total
        if m9.falta <= 0:
            m9.falta = 'Passou'
    if x == 'Geografia':
        m10.notas.append(float(input_nota.get()))
        m10.total = sum(m10.notas)
        m10.falta = 7 - m10.total
        if m10.falta <= 0:
            m10.falta = 'Passou'
    if x == 'Sociologia':
        m11.notas.append(float(input_nota.get()))
        m11.total = sum(m11.notas)
        m11.falta = 7 - m11.total
        if m11.falta <= 0:
            m11.falta = 'Passou'
    if x == 'Filosofia':
        m12.notas.append(float(input_nota.get()))
        m12.total = sum(m12.notas)
        m12.falta = 7 - m12.total
        if m12.falta <= 0:
            m12.falta = 'Passou'
    print(m1.total, m2.total, m3.total, m4.total, m5.total, m6.total, m7.total, m8.total, m9.total, m10.total, m11.total, m12.total)
    

menu = ctk.CTkOptionMenu(app, values= ['Matemática', 'Biologia', 'Física', 'Química', 'Português', 'Literatura', 'Espanhol', 'Inglês', 'História', 'Geografia', 'Sociologia', 'Filosofia'], command= select)
menu.place(x=15, y=10)


def abrir_aba():
    value = [['#', 'Av1', 'Av2', 'Av3', 'Av4', 'Av5', 'Total', 'Falta'],
             ['Mat', '', '', '', '', '', m1.total, m1.falta],
             ['Bio', '', '', '', '', '', m2.total, m2.falta],
             ['Fis', '', '', '', '', '', m3.total, m3.falta],
             ['Qui', '', '', '', '', '', m4.total, m4.falta],
             ['Port', '', '', '', '', '', m5.total, m5.falta],
             ['Lit', '', '', '', '', '', m6.total, m6.falta],
             ['Esp', '', '', '', '', '', m7.total, m7.falta],
             ['Ing', '', '', '', '', '', m8.total, m8.falta],
             ['Hist', '', '', '', '', '', m9.total, m9.falta],
             ['Geo', '', '', '', '', '', m10.total, m10.falta],
             ['Socio', '', '', '', '', '', m11.total, m11.falta],
             ['Filo', '', '', '', '', '', m12.total, m12.falta]]
    
    nova_aba = ctk.CTkToplevel(app)
    nova_aba.title('Boletim')
    nova_aba.geometry('600x400')
    tabela = CTkTable(nova_aba, row=13, column=8, values= value)
    tabela.pack(padx=20, pady=20)

    # Inserindo Mat
    tabela.insert(row=1, column=1, value=m1.notas[0])
    tabela.insert(row=1, column=2, value=m1.notas[1])
    tabela.insert(row=1, column=3, value=m1.notas[2])
    tabela.insert(row=1, column=4, value=m1.notas[3])
    # tabela.insert(row=1, column=5, value=m1.notas[4])

    # # Inserindo Bio
    # tabela.insert(row=2, column=1, value=m2.notas[0])
    # tabela.insert(row=2, column=2, value=m2.notas[1])
    # tabela.insert(row=2, column=3, value=m2.notas[2])
    # tabela.insert(row=2, column=4, value=m2.notas[3])
    # tabela.insert(row=2, column=5, value=m2.notas[4])

    # # Inserindo Fis
    # tabela.insert(row=3, column=1, value=m3.notas[0])
    # tabela.insert(row=3, column=2, value=m3.notas[1])
    # tabela.insert(row=3, column=3, value=m3.notas[2])
    # tabela.insert(row=3, column=4, value=m3.notas[3])
    # tabela.insert(row=3, column=5, value=m3.notas[4])

    # # Inserindo Quim
    # tabela.insert(row=4, column=1, value=m4.notas[0])
    # tabela.insert(row=4, column=2, value=m4.notas[1])
    # tabela.insert(row=4, column=3, value=m4.notas[2])
    # tabela.insert(row=4, column=4, value=m4.notas[3])
    # tabela.insert(row=4, column=5, value=m4.notas[4])


botao_aba = ctk.CTkButton(app, text='Ver notas', command=abrir_aba, width=120)
botao_aba.place(x=130, y=210)



# Tratando o DB

db_path = Path(__file__).parent / 'db.json'
db = TinyDB(db_path, indent=4)



app.mainloop()