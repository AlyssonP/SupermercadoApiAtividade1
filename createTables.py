import sqlite3

conn = sqlite3.connect("dataset.db")
dbCursor = conn.cursor()

dbCursor.execute("""
CREATE TABLE produtos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(200) NOT NULL 
)
""")

dbCursor.execute("""
CREATE TABLE usuarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(200) NOT NULL
)
""")

dbCursor.execute("""
CREATE TABLE setores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(200) NOT NULL
)
""")

dbCursor.execute("""
CREATE TABLE categorias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(200) NOT NULL
)
""")

print("Tabelas de Produtos, Usuários, Setores e Categorias criadas.")

conn.close()