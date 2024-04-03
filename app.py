from flask import Flask, request
from Controllers import getProdutos, getProduto, createProduto, getUsuarios, getUsuario, createUsuario, getSetores, getSetor, createSetor, getCategorias, getCategoria, createCategoria

api = Flask(__name__)

@api.get("/")
def index():
  return {"version":1.0}

# CRUD Produtos
@api.get("/produtos")
def produtos():
  produtos = [ {"id":prod.id, "nome": prod.nome} for prod in getProdutos()]
  return (produtos, 200)

@api.get("/produtos/<int:id>")
def produto(id: int):
  produto = getProduto(id)
  if(produto != None):
    return ({"id":produto.id, "nome":produto.nome}, 200)
  return ({"msg": "Not Found"}, 404)

@api.post("/produtos")
def postProduto():
  dataResquest = request.get_json()
  
  if("nome" not in dataResquest):
    return ({"msg":"Name field is mandatory"}, 404)
  
  if(createProduto(dataResquest["nome"])):
    return ({"msg":"Product created"}, 201)
  
  return ({"msg":"There was an error when creating product"}, 500)

# CRUD Usuarios
@api.get("/usuarios")
def usuarios():
  usuarios = [{"id":user.id, "nome": user.nome} for user in getUsuarios()]
  return usuarios

@api.get("/usuarios/<int:id>")
def usuario(id: int):
  usuario = getUsuario(id)
  if(usuario != None):
    return ({"id": usuario.id, "nome":usuario.nome}, 200)
  return ({"msg": "Not Found"}, 404)

@api.post("/usuarios")
def postUsuario():
  dataResquest = request.get_json()
  
  if("nome" not in dataResquest):
    return ({"msg":"Name field is mandatory"}, 404)
  
  if(createUsuario(dataResquest["nome"])):
    return ({"msg":"User created"}, 201)
  
  return ({"msg":"There was an error when creating user"}, 500)

# CRUD Setores
@api.get("/setores")
def setores():
  setores = [{"id":setor.id, "nome":setor.nome} for setor in getSetores()]
  return (setores, 200)

@api.get("/setores/<int:id>")
def setor(id: int):
  setor = getSetor(id)
  if(setor != None):
    return ({"id":setor.id, "nome":setor.nome}, 200)
  return ({"msg": "Not Found"}, 404)

@api.post("/setores")
def postSetores():
  dataResquest = request.get_json()
  
  if("nome" not in dataResquest):
    return ({"msg":"Name field is mandatory"}, 404)
  
  if(createSetor(dataResquest["nome"])):
    return ({"msg":"Setor created"}, 201)
  
  return ({"msg":"There was an error when creating setor"}, 500)

# CRUD Categorias
@api.get("/categorias")
def categorias():
  categorias = [{"id":categoria.id, "nome":categoria.nome} for categoria in getCategorias()]
  return (categorias, 200)

@api.get("/categorias/<int:id>")
def categoria(id: int):
  categoria = getCategoria(id)
  if(categoria != None):
    return ({"id":categoria.id, "nome":categoria.nome}, 200)
  return ({"msg": "Not Found"}, 404)

@api.post("/categorias")
def postCategoria():
  dataResquest = request.get_json()
  
  if("nome" not in dataResquest):
    return ({"msg":"Name field is mandatory"}, 404)
  
  if(createCategoria(dataResquest["nome"])):
    return ({"msg":"Category created"}, 201)
  
  return ({"msg":"There was an error when creating category"}, 500)

