import sqlite3

def criar_tabela():
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS galaxias
                  (id INTEGER PRIMARY KEY, nome TEXT, estrelaPrincipal TEXT, distancia INTEGER, imagem TEXT)''')
    conn.commit()
    conn.close()

def inserir_galaxia(nome, estrelaPrincipal, distancia, imagem):
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO galaxias (nome, estrelaPrincipal, distancia, imagem) VALUES (?, ?, ?, ?)', (nome, estrelaPrincipal, distancia, imagem))
    conn.commit()
    conn.close()

def deletar_galaxia(id):
        conn = sqlite3.connect('galaxias.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM galaxias WHERE id = ?', (id,))
        galaxia = cursor.fetchone()
        if galaxia:
            cursor.execute('DELETE FROM galaxias WHERE id = ?', (id,))
        conn.commit()
        conn.close()
def atualizar_galaxia(id, nome, estrelaPrincipal, distancia, imagem):
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE galaxias SET nome = ?, estrelaPrincipal = ?, distancia = ?, imagem = ? WHERE id = ?', (nome, estrelaPrincipal, distancia, imagem, id))
    conn.commit()
    conn.close()

def retornar_galaxia(id):
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM galaxias WHERE id = ?', (id,))
    galaxia = cursor.fetchone()
    conn.close()
    if galaxia:
        return {
            'id': galaxia[0],
            'nome': galaxia[1],
            'estrelaPrincipal': galaxia[2],
            'distancia': galaxia[3],
            'imagem': galaxia[4]
        }
    return {}

def listar_galaxias():
    resultado = []
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM galaxias')
    galaxias = cursor.fetchall()
    conn.close()
    #Como precisamos devolver em JSON já não deixaremos em tuplas e sim em lista por isso percorremos em for as tuplas e as deixamos em uma lista
    for item in galaxias:
        galaxia = {
            'id': item[0],
            'nome': item[1],
            'estrelaPrincipal': item[2],
            'distancia': item[3],
            'imagem': item[4]
        }
        resultado.append(galaxia)

    return resultado


