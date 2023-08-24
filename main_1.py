import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

#Criando a tabela chamada "Estudantes" com os seguintes campos:
cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER
);
""")

#criando os dados dos alunos    
alunos = [
        ('Ana Silva', 'Computação', '2019'),
        ('Pedro Mendes', 'Física', '2021'),
        ('Carla Souza', 'Computação', '2020'),
        ('João Alves', 'Matemática', '2018'),
        ('Maria Oliveira', 'Química', '2022')
]

#inserindo os valores dos alunos na tabela
cursor.executemany("""
INSERT INTO Alunos (Nome, Curso, Ano_de_Ingresso)
VALUES (?, ?, ?);
""", alunos)

#commit na base de dados 
conn.commit()

#pegandos apenas os alnos que tem o ano de ingresso entre 2019-2020
#"for aluno from alunos:
#  if aluno["ano_de_ingresso"] == 2019 or if aluno["ano_de_ingresso"] == 2020:
#       print(aluno)"
cursor.execute("SELECT * FROM Alunos WHERE Ano_de_Ingresso BETWEEN 2019 AND 2020; ")

#printando apenas os alunos selecionados 
print(cursor.fetchall())

#trocando o ano de ingersso de um dos alunos 
cursor.execute("UPDATE Alunos SET Ano_de_Ingresso = 1789 WHERE ID = 1")
conn.commit()

#printando todos os alunos para verificar a mudança do ano de ingresso 
cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())

#dell no primeiro alunos, que apressenta o id=1
cursor.execute("DELETE FROM Alunos WHERE ID = 1")
conn.commit()

#printando todos os alunos para verificar a retirada do primeiro aluno 
cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())

#pegando os alunos que fazem ccomp e ingerssaram depois de 2019
#""for aluno in alunos:
#       if aluno["Curso"] == 'Computação' and aluno["Ano_de_Ingresso"] > 2019:
#           print(aluno)"""
cursor.execute("SELECT * FROM Alunos WHERE Curso = 'Computação' AND Ano_de_Ingresso > 2019")
conn.commit()
print(cursor.fetchall())

#mudando todos os alunos de ccomp para ano de ingresso em 2018
cursor.execute("UPDATE Alunos SET Ano_de_Ingresso = 2018 WHERE Curso = 'Computação'")
conn.commit()
cursor.execute("SELECT * FROM Alunos")
print(cursor.fetchall())