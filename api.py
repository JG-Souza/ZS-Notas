from storage import cursor

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



# Passando valores para matérias no momento da inicialização do APP

def persiste_dados(objeto, linha, materia, local):
    result_notas = cursor.execute("SELECT nota FROM boletim WHERE materia = ?", [materia]).fetchall()
    objeto.notas.extend([nota[0] for nota in result_notas])
    objeto.total = sum(objeto.notas)
    local.insert(row=linha, column=6, value=objeto.total)
    objeto.falta = 7 - objeto.total
    if objeto.falta <= 0:
        objeto.falta = 'Passou'
    local.insert(row=linha, column=7, value=objeto.falta)