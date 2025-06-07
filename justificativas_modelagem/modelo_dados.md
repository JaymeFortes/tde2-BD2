# Justificativas de Modelagem dos Dados

## Coleção de Clientes
Decidimos colocar todas as informações do cliente em um só lugar, os endereços ficam dentro do documento do cliente porque assim não precisamos buscar em vários lugares diferentes quando queremos ver os dados completos. O mesmo vale para os telefones, como cada cliente não tem muitos telefones, faz mais sentido deixar tudo junto.
Para clientes pessoa física e pessoa jurídica, criamos seções separadas dentro do mesmo documento, a pessoa física tem CPF, data de nascimento e gênero, e a pessoa jurídica tem CNPJ e razão social. Dessa forma, evitamos campos vazios desnecessários e cada tipo de cliente tem exatamente o que precisa. Podemos buscar clientes por região, cidade ou estado sem complicação, e também conseguimos pegar todas as informações do cliente de uma vez só, sem precisar procurar em várias tabelas diferentes.

## Coleção de Produtos
Cada produto tem suas informações de categoria dentro do próprio documento, e como as categorias não mudam com frequência, faz sentido deixar tudo junto para acelerar as consultas. Quando listamos produtos por categoria, não precisamos buscar informações em outros lugares, criamos regras de validação para garantir que os dados estejam sempre corretos. Por exemplo, o campo "importado" só aceita "Sim" ou "Não", e as datas têm formato específico, isso evita erros na hora de cadastrar produtos.
Com essa estrutura, conseguimos filtrar produtos por categoria, preço, se é importado ou não, e prazo de entrega de forma bem rápida. Também podemos separar por área de atuação quando necessário.

## Coleção de Pedidos
Os itens do pedido ficam dentro do próprio documento do pedido. Cada item tem o código do produto, quantidade e valor unitário, assim conseguimos calcular o total do pedido rapidamente, sem precisar buscar informações em outros lugares. As informações de entrega também ficam no pedido, incluindo dados do motorista e data, para o cliente, usamos apenas o código dele no pedido, não todas as informações. Isso evita duplicar dados que podem mudar com o tempo, como endereço ou telefone do cliente.
Essa organização permite ver todos os itens e custos do pedido de uma vez, podemos cruzar com os dados do cliente quando necessário, mas mantemos o histórico da entrega completo e inalterado dentro do pedido.
