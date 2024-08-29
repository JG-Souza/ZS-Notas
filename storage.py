import sqlite3


# Iniciando meu DB

con = sqlite3.connect('data.db', check_same_thread= False)
query_criar_tabela = '''CREATE TABLE IF NOT EXISTS boletim
(id INT AUTO INCREMENT, materia TEXT, notaref TEXT, nota INT)
'''
con.execute(query_criar_tabela)
cursor = con.cursor()

