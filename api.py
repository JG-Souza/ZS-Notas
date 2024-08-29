from main import cursor, tabela

# Passando valores para matérias no momento da inicialização do APP

def persiste_dados(objeto, linha, materia):
    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", [materia]).fetchall()
    objeto.notas.extend([nota[0] for nota in result_notas])
    objeto.total = sum(objeto.notas)
    tabela.insert(row=linha, column=6, value=objeto.total)
    objeto.falta = 7 - objeto.total
    if objeto.falta <= 0:
        objeto.falta = 'Passou'
    tabela.insert(row=linha, column=7, value=objeto.falta)