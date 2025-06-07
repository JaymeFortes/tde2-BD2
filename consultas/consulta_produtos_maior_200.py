# Consulta: Listar todos os produtos com preço acima de R$ 200

res = bd.produtos.find(
    { "preco": { "$gt": 200.0 } },
    { "_id": 1, "titulo": 1, "preco": 1 }
)

for doc in res:
    print(doc)
