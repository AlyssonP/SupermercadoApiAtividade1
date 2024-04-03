import sqlite3

conn = sqlite3.connect("dataset.db")
dbCursor = conn.cursor()

dbCursor.execute("""
                 INSERT INTO produtos (nome) VALUES
                 ('Margarina B+'),
                 ('Shampoo C+');
                 """)

dbCursor.execute("""
                 INSERT INTO usuarios (nome) VALUES
                 ('José');
                 """)

dbCursor.execute("""
                 INSERT INTO setores (nome) VALUES
                 ('Alimentos'),
                 ('Higiene e limpeza')
                 """)

dbCursor.execute("""
                 INSERT INTO categorias (nome) VALUES
                 ('Margarinas e Mantegas'),
                 ('Shampos');
                 """)

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()