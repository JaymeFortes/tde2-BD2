# Consulta: Listar todos os produtos com preço acima de R$ 200

res = bd.produtos.find(
    { "preco": { "$gt": 200.0 } },
    { "_id": 1, "titulo": 1, "preco": 1 }
)

for doc in res:
    print(doc)



# Consulta: Total de pedidos por cliente

res = bd.pedidos.aggregate([
    {
        "$group": {
            "_id": "$cod_cliente",
            "total_pedidos": { "$sum": 1 }
        }
    },
    {
        "$lookup": {
            "from": "clientes",
            "localField": "_id",
            "foreignField": "_id",
            "as": "cliente"
        }
    },
    { "$unwind": "$cliente" },
    {
        "$project": {
            "cliente_id": "$_id",
            "nome": "$cliente.nome",
            "total_pedidos": 1,
            "_id": 0
        }
    },
    { "$sort": { "total_pedidos": -1 } }
])

for doc in res:
    print(doc)

