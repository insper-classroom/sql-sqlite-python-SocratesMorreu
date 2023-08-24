import sqlite3

#funcao criando tabela
def cria_tabela():
    # Conexão com o banco de dados dentro da pasta "db"
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    #Criando a tabela com os seguintes campos:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alunos (
        ID INTEGER PRIMARY KEY,
        Nome TEXT,
        Curso TEXT,
        "Ano de Ingresso" INTEGER
    )
    ''')

    conn.commit()
    conn.close()

#funcao inserindo registro 
def insere_registro(nome, curso, ano):
    # Conexão com o banco de dados dentro da pasta "db"
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    #inserindo os valores dos alunos na tabela
    cursor.execute('INSERT INTO Alunos (Nome, Curso, "Ano de Ingresso") VALUES (?, ?, ?)', (nome, curso, ano))

    conn.commit()
    conn.close()

#funcao para inserir registros 
def consulta_registros(ano):
    # Conexão com o banco de dados dentro da pasta "db"
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    #pegando apenas os alunos do ano selecionado
    cursor.execute('SELECT * FROM Alunos WHERE "Ano de Ingresso" = ?', (ano,))
    registros = cursor.fetchall()

    conn.close()
    return registros

#funcao que atualiza registro 
def atualiza_registro(id, novo_ano):
    # Conexão com o banco de dados dentro da pasta "db"
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    #atualiza o registro a partitr do id e ano dados 
    cursor.execute('UPDATE Alunos SET "Ano de Ingresso" = ? WHERE ID = ?', (novo_ano, id))

    conn.commit()
    conn.close()

#funcao que deleta um registro 
def deleta_registro(id):
    # Conexão com o banco de dados dentro da pasta "db"
    conn = sqlite3.connect('db/livros_database.db')
    cursor = conn.cursor()

    #deleta o aluno do id selecionado 
    cursor.execute('DELETE FROM Alunos WHERE ID = ?', (id,))

    conn.commit()
    conn.close()