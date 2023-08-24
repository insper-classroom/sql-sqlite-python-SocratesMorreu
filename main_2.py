from db import db_utils as db 
import sqlite3

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/livros_database.db')
cursor = conn.cursor()

db.cria_tabela()

db.insere_registro('Pope Francis', 'Musculacao', 1789) 

db.insere_registro('Fulcrum', 'Bejamincity', 2017) 

db.consulta_registros(2020)

db.atualiza_registro(6, 1789)

db.deleta_registro(2)

#printando apos as alteracoes 
cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())