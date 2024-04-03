import sqlite3
from typing import List
from Models import Produto, Usuario, Setor, Categoria
DATABASE_NAME = "dataset.db"

def getDB():
  conn = sqlite3.connect(DATABASE_NAME)
  return conn

# Controllers Produtos
def getProdutos() -> List[Produto]:
  db = getDB()
  cursor = db.cursor()
  query = "SELECT * FROM produtos;"
  cursor.execute(query)
  produtos = [Produto(prod[0], prod[1]) for prod in cursor.fetchall()]
  db.close()
  return produtos
  
def getProduto(id: int) -> Produto:
  db = getDB()
  cursor = db.cursor()
  statement = "SELECT * FROM produtos WHERE id = ?;"
  cursor.execute(statement, [id])
  resultSet = cursor.fetchall()
  if(len(resultSet) != 0):
    return Produto(resultSet[0][0], resultSet[0][1])
  
  return None
  
def createProduto(nome: str):
  db = getDB()
  cursor = db.cursor()
  statement = "INSERT INTO produtos (nome) VALUES (?);"
  cursor.execute(statement, [nome])
  db.commit()
  db.close()
  return True

# Controllers Usuários
def getUsuarios() -> List[Usuario]:
  db = getDB()
  cursor = db.cursor()
  query = "SELECT * FROM usuarios;"
  cursor.execute(query)
  usuarios = [Produto(user[0], user[1]) for user in cursor.fetchall()]
  db.close()
  return usuarios

def getUsuario(id: int) -> Usuario:
  db = getDB()
  cursor = db.cursor()
  statement = "SELECT * FROM usuarios WHERE id = ?;"
  cursor.execute(statement, [id])
  resultSet = cursor.fetchall()
  if(len(resultSet) != 0):
    return Usuario(resultSet[0][0], resultSet[0][1])
  
  return None
  
def createUsuario(nome: str):
  db = getDB()
  cursor = db.cursor()
  statement = "INSERT INTO usuarios (nome) VALUES (?);"
  cursor.execute(statement, [nome])
  db.commit()
  db.close()
  return True

# Controllers Setores
def getSetores() -> List[Setor]:
  db = getDB()
  cursor = db.cursor()
  query = "SELECT * FROM setores;"
  cursor.execute(query)
  setores = [Setor(setor[0], setor[1]) for setor in cursor.fetchall()]
  db.close()
  return setores

def getSetor(id: int) -> Setor:
  db = getDB()
  cursor = db.cursor()
  statement = "SELECT * FROM setores WHERE id = ?;"
  cursor.execute(statement, [id])
  resultSet = cursor.fetchall()
  if(len(resultSet) != 0):
    return Setor(resultSet[0][0], resultSet[0][1])
  
  return None
  
def createSetor(nome: str):
  db = getDB()
  cursor = db.cursor()
  statement = "INSERT INTO setores (nome) VALUES (?);"
  cursor.execute(statement, [nome])
  db.commit()
  db.close()
  return True


# Controllers Categorias
def getCategorias() -> List[Categoria]:
  db = getDB()
  cursor = db.cursor()
  query = "SELECT * FROM categorias;"
  cursor.execute(query)
  categorias = [Categoria(categoria[0], categoria[1]) for categoria in cursor.fetchall()]
  db.close()
  return categorias

def getCategoria(id: int) -> Categoria:
  db = getDB()
  cursor = db.cursor()
  statement = "SELECT * FROM categorias WHERE id = ?;"
  cursor.execute(statement, [id])
  resultSet = cursor.fetchall()
  if(len(resultSet) != 0):
    return Categoria(resultSet[0][0], resultSet[0][1])
  
  return None
  
def createCategoria(nome: str):
  db = getDB()
  cursor = db.cursor()
  statement = "INSERT INTO categorias (nome) VALUES (?);"
  cursor.execute(statement, [nome])
  db.commit()
  db.close()
  return True
