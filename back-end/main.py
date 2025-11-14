from fastapi import FastAPI
import funcao 

app = FastAPI(title="Gerenciador de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao Gerenciador de Produtos"}

@app.post("/produtos")
def criar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.cadastrar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto cadastrado com sucesso!"}


