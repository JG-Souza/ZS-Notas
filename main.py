import customtkinter as ctk
from CTkTable import *
from api import persiste_dados, value, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12
from storage import cursor, con


# Criando janela
app = ctk.CTk()
app.geometry('800x800')
app.title('ZS Notas')
    

tabela = CTkTable(app, row=13, column=8, values= value)
tabela.pack(padx=20, pady=20)


# Dicionário que mapeia o nome da matéria para suas instâncias e linhas na tabela
materias = {
    'Matemática': (m1, 1),
    'Biologia': (m2, 2),
    'Física': (m3, 3),
    'Química': (m4, 4),
    'Português': (m5, 5),
    'Literatura': (m6, 6),
    'Espanhol': (m7, 7),
    'Inglês': (m8, 8),
    'História': (m9, 9),
    'Geografia': (m10, 10),
    'Sociologia': (m11, 11),
    'Filosofia': (m12, 12)
}


# Processa cada matéria usando o dicionário
for materia, (objeto, linha) in materias.items():
    persiste_dados(objeto, linha, materia, tabela)


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


def select(self):
    global btn_sbt
    global x
    global input_nota
    # Obtém a seleção do menu e armazena na variável 'x'
    x = menu.get()
    
    # Verifica se a matéria selecionada está no dicionário 'materias'
    if x in materias:
        # Define o texto do placeholder com base na matéria selecionada
        placeholder_text = f'Nota {x[:3]}'
        
        # Cria o CTkEntry com o texto do placeholder
        input_nota = ctk.CTkEntry(app, placeholder_text=placeholder_text)
        input_nota.place(x=325, y=490)

    # Cria o botão submit
    btn_sbt = ctk.CTkButton(app, text='enviar',  fg_color='#A020F0', hover_color='#9400D3',command=submit, width= 60,)
    btn_sbt.place(x=365, y=530)

def destruir_widgets(widgets):
    # Destrói uma lista de widgets fornecida
    for widget in widgets:
        widget.destroy()
    

def inserir_nota(materia_obj, row, nota_ref, input_nota, column):
    # Verifica se a nota já foi inserida
    notasref = cursor.execute("SELECT notaref FROM boletim WHERE materia = ? AND notaref = ?", [materia_obj.nome, nota_ref]).fetchone()
    if notasref is None:
        # Insere a nota no banco de dados
        query_inserir_data = '''INSERT INTO boletim (materia, notaref, nota) VALUES (?, ?, ?)'''
        tupla_inserir_dados = (materia_obj.nome, nota_ref, input_nota.get())
        cursor.execute(query_inserir_data, tupla_inserir_dados)
        con.commit()
        
        # Atualiza a tabela com a nova nota
        tabela.insert(row=row, column=column, value=cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", [materia_obj.nome, nota_ref]).fetchone())
        
        # Atualiza as notas da matéria e a tabela
        result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", [materia_obj.nome]).fetchall()
        materia_obj.notas = [nota[0] for nota in result_notas]
        materia_obj.total = sum(materia_obj.notas)
        tabela.insert(row=row, column=6, value=materia_obj.total)
        materia_obj.falta = 7 - materia_obj.total
        if materia_obj.falta <= 0:
            materia_obj.falta = 'Passou'
        tabela.insert(row=row, column=7, value=materia_obj.falta)


def submit():
    z = spinbox2.get()
    materia_obj, row = materias.get(x, (None, None))
    
    if materia_obj and len(materia_obj.notas) <= 4:
        nota_ref_map = {
            '1ª': ('n1', 1),
            '2ª': ('n2', 2),
            '3ª': ('n3', 3),
            '4ª': ('n4', 4),
            '5ª': ('n5', 5)
        }
        nota_ref, column = nota_ref_map.get(z, (None, None))
        
        if nota_ref:
            inserir_nota(materia_obj, row, nota_ref, input_nota, column)

    # Resetando os botões (Despoluindo a tela)
    widgets_para_destruir = [btn_sbt, input_nota, menu, spinbox2]
    destruir_widgets(widgets_para_destruir)


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
     # Obtém a seleção do menu e armazena na variável 'x'
    y = menu_edit.get()
    
    # Verifica se a matéria selecionada está no dicionário 'materias'
    if y in materias:
        # Define o texto do placeholder com base na matéria selecionada
        placeholder_text = f'Nota {y[:3]}'
        
        # Cria o CTkEntry com o texto do placeholder
        input_nota_edit = ctk.CTkEntry(app, placeholder_text=placeholder_text)
        input_nota_edit.place(x=325, y=490)


    btn_att = ctk.CTkButton(app, text='atualizar', command=att, width= 60, fg_color='#A020F0', hover_color='#9400D3')
    btn_att.place(x=365, y=530)


# Função para destruir todos os widgets
def destruir_widgets_edit(widgets_edit):
    for widget in widgets_edit:
        if widget and widget.winfo_exists():
            widget.destroy()


# Lógica por trás do Edit das notas
def att():
    editz = spinbox.get()
    if y in materias:
        # Obtém o objeto da matéria e a linha da tabela a partir do dicionário
        obj_materia, row = materias[y]
        
        # Mapeia o semestre para a referência da nota
        notaref_map = {
            '1ª': 'n1',
            '2ª': 'n2',
            '3ª': 'n3',
            '4ª': 'n4',
            '5ª': 'n5'
        }
        
        notaref = notaref_map.get(editz)
        if not notaref:
            return
        
        # Atualiza a nota no banco de dados
        query_atualizar_dados = '''UPDATE boletim
                                   SET nota = ?
                                   WHERE notaref = ? AND materia = ?'''
        tupla_atualizar_dados = (input_nota_edit.get(), notaref, y)
        cursor.execute(query_atualizar_dados, tupla_atualizar_dados)
        con.commit()
        
        # Atualiza a tabela com a nova nota
        tabela.insert(row=row, column={'1ª': 1, '2ª': 2, '3ª': 3, '4ª': 4, '5ª': 5}[editz],
                      value=cursor.execute("SELECT nota FROM boletim WHERE materia = ? AND notaref = ?", [y, notaref]).fetchone())
        
        # Atualiza as notas da matéria e a tabela
        result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", [y]).fetchall()
        obj_materia.notas = [nota[0] for nota in result_notas]
        obj_materia.total = sum(obj_materia.notas)
        tabela.insert(row=row, column=6, value=obj_materia.total)
        obj_materia.falta = 7 - obj_materia.total
        if obj_materia.falta <= 0:
            obj_materia.falta = 'Passou'
        tabela.insert(row=row, column=7, value=obj_materia.falta)

    # Lista dos widgets a serem destruídos
    widgets_para_destruir = [menu_edit, spinbox, input_nota_edit, btn_att]
    
    # Destruir todos os widgets
    destruir_widgets_edit(widgets_para_destruir)


# Menu Option para escolher a matéria 
def Editar():
    global menu_edit
    menu_edit = ctk.CTkOptionMenu(app, values= ['Matemática', 'Biologia', 'Física', 'Química', 'Português', 'Literatura', 'Espanhol', 'Inglês', 'História', 'Geografia', 'Sociologia', 'Filosofia'], command=select_spb, fg_color='#A020F0', button_color='#A020F0', button_hover_color='#9400D3',dropdown_hover_color='#A020F0')
    menu_edit.place(x=281, y=450)

btn_editar = ctk.CTkButton(app, text='Editar', command= Editar, width=100, fg_color='#A020F0', hover_color='#9400D3')
btn_editar.place(x=417, y=410)


app.mainloop()