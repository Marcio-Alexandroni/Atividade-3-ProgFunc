# Atividade-3-ProgFunc

Web para Processamento Concorrente e Transacional de Pedidos
Uma startup de comércio eletrônico está desenvolvendo uma nova plataforma para processar
pedidos de forma rápida, segura e escalável. A aplicação deverá garantir que múltiplos pedidos
possam ser tratados simultaneamente (explorando concorrência e paralelismo), mantendo ao
mesmo tempo a consistência e integridade dos dados via transações atômicas.
Além disso, a plataforma deverá oferecer uma interface web simples baseada em Flask, permitindo
que usuários simulem pedidos e consultem relatórios por meio de chamadas HTTP.
Objetivo:
Você foi contratado para projetar e implementar uma aplicação capaz de:
 Processar vários pedidos de compra concorrentes, simulando o comportamento de múltiplos
usuários comprando ao mesmo tempo.
 Utilizar transações para garantir que cada pedido seja executado de forma atômica e consistente,
mesmo em caso de falhas (como falta de saldo ou estoque).
 Disponibilizar uma API RESTful para que o sistema possa receber e consultar pedidos via
requisições HTTP.
 Utilizar concorrência/paralelismo real com ThreadPoolExecutor ou ProcessPoolExecutor.
 Armazenar dados de clientes, produtos e pedidos em um banco de dados relacional utilizando
SQLAlchemy.
Requisitos Funcionais
1. Cadastro de dados iniciais:
 Tabela de clientes com nome e saldo disponível.
 Tabela de produtos com nome, preço e estoque.
2. Processamento de pedidos:
2
 Um pedido consiste em:
 Escolha aleatória de um cliente e um produto.
 Verificação de saldo do cliente e estoque do produto.
 Criação do pedido e dos itens de pedido.
 Atualização do saldo do cliente e do estoque do produto.
 Toda operação de pedido deve ser executada dentro de uma transação.
 Se algum erro ocorrer (ex: saldo insuficiente), nenhuma alteração deve ser
persistida.
3. Execução concorrente:
 O sistema deve ser capaz de processar múltiplos pedidos ao mesmo tempo, utilizando um
pool de threads ou processos.
4. API Web com Flask:
 POST /pedido: simula a chegada de um novo pedido (executado em paralelo).
 GET /relatorio: retorna os pedidos processados com sucesso.
 (Opcional) GET /status: informa número de pedidos em andamento ou concluídos.
Requisitos Técnicos:
 Linguagem: Python 3.x
 Banco de dados: MySQL
 ORM: SQLAlchemy
 Web framework: Flask
 Concorrência: ThreadPoolExecutor (ou ProcessPoolExecutor)
 Uso explícito de transações (session.begin())
 Organização modular em arquivos separados (app.py, models.py, etc.)
Entregáveis:
 Código-fonte bem estruturado e modular.
 Script de criação e povoamento do banco de dados.
 Arquivo README.md com instruções para instalação, execução e teste da API.
 Testes com pelo menos 20 pedidos simultâneos, mostrando o tratamento de concorrência e
rollback em falhas.
