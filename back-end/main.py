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


@app.get("/produtos")
def listar_produto():
    produtos = funcao.listar_produto()
    lista = []
    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
        return {"produtos": lista}
    
@app.put("/produtos/{id}")
def atualizar_produto(id: int, novo_preco: float, nova_quantidade: int):
    produto = funcao.buscar_produto(id)
    if produto:
        funcao.atualizar_produto(id, novo_preco, nova_quantidade)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado."}

