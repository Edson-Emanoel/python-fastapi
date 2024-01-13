from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: { "item": "jogo1", "quantidade": 4, "valor": 125 },
    2: { "item": "jogo2", "quantidade":14, "valor": 225 },
    3: { "item": "jogo3", "quantidade":24, "valor": 325 },
}

@app.get("/")
def home():
    return {"vendas": len(vendas)}


@app.get("/vendas/{id}")
def pegar_venda(id: int):
    return vendas[id]

# para rodar o projeto
# uvicorn app:app2 --reload
# url gerada :: http://localhost:8000/docs
