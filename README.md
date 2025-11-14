# Atividade API - Controle de Produtos e Estoque
## Função 
- Adicionar produto
- Listar todos
- Atualizar preço ou quantidade 
- Excluir produtos da tabela

# Como usar?
## DOCS
Entre no .venv
- Instale os requirements.txt no terminal Bash 

pip install dotenv fastapi psycopg2-binary psycopg2 
uvicorn

Entre na pasta back-end
- Rode o main.py no terminal 

uvicorn main:app -- reload

## SITE STREAMLIT

Entre na pasta front-end
- Rode o app.py no terminal

python -m streamlit run app.py 

## Instalar o requirements.txt
- Entre no ambiente virtual .venv
Windows (PowerShell): 
.\\.venv\Scripts\activate

Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt 

