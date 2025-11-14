import streamlit as st
import requests 

# Rodar o streamlit
# python -m streamlit run app.py

# URL da API Fastapi
API_URL = "http://127.0.0.1:8000"

st.title("📦 Sistema de Controle de Produtos")

menu = st.sidebar.selectbox(
    "Menu",
    ["Listar Produtos", "Cadastrar Produtos", "Atualizar Produtos", "Deletar Produtos"]
)

if menu == "Listar Produtos":
    st.subheader("📦 Todos os produtos")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado ainda!")
    else:
        st.error("Erro ao conectar com a API.")





