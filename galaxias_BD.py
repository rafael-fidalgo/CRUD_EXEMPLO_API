import sqlite3

# abaixo será definido as funções que serão utilizadas  dentro das rotas para realização do CRUD.


# função para criar uma tabela onde é definido as seguintes colunas: um id como chave primaria, além do nome, estrela principal, uma imagem e a distância.
def criar_tabela():
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS galaxias
                (id INTEGER PRIMARY KEY, nome TEXT, estrelaPrincipal TEXT, distancia INTEGER, imagem TEXT)''')
    conn.commit()
    conn.close()


#função que permite criação de uma nova galaxia no banco de dados.
def inserir_galaxia(nome, estrelaPrincipal, distancia, imagem):
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO galaxias (nome, estrelaPrincipal, distancia, imagem) VALUES (?, ?, ?, ?)', (nome, estrelaPrincipal, distancia, imagem))
    conn.commit()
    conn.close()


#função que permite exclusão de uma nova galaxia no banco de dados.
def deletar_galaxia(id):
        conn = sqlite3.connect('galaxias.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM galaxias WHERE id = ?', (id,))
        galaxia = cursor.fetchone()
        if galaxia:
            cursor.execute('DELETE FROM galaxias WHERE id = ?', (id,))
        conn.commit()
        conn.close()

#função que permite atualização de todos os dados de uma nova galaxia no banco de dados.        
def atualizar_galaxia(id, nome, estrelaPrincipal, distancia, imagem):
    conn = sqlite3.connect('galaxias.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE galaxias SET nome = ?, estrelaPrincipal = ?, distancia = ?, imagem = ? WHERE id = ?', (nome, estrelaPrincipal, distancia, imagem, id))
    conn.commit()
    conn.close()

#função que possibilita listar uma galaxia especifica dentro de um banco de dados a partir de um id.
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

#função que possibilita listar todas as galaxias dentro de um banco de dados. 
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


