# Sistema de CRUD de Veículos com Sockets

Este projeto implementa um sistema básico de **CRUD** (Create, Read, Update, Delete) para gerenciar veículos, utilizando **sockets TCP** para comunicação entre o cliente e o servidor. O servidor mantém uma lista de veículos em memória, e o cliente pode enviar comandos para criar, ler, atualizar ou excluir veículos, bem como encerrar a conexão.

## Requisitos

- **>=Python 3.10**
- Bibliotecas padrão do Python (sem dependências externas)

## Estrutura dos Arquivos

- server.py: Implementa o servidor TCP, que escuta por conexões e processa comandos para gerenciar veículos.
- client.py: Implementa o cliente TCP, que envia comandos para o servidor e recebe as respostas.

## Como Executar

### 1. Iniciar o Servidor

Para iniciar o servidor, execute o script server.py:

bash
python server.py
O servidor ficará ouvindo conexões na porta 5000.

## 2. Iniciar o Cliente
Em outro terminal, execute o cliente:

bash
Copiar código
python client.py
Você poderá enviar comandos para o servidor através do terminal do cliente.

## Comandos Suportados
Os comandos devem ser enviados no formato especificado abaixo, utilizando o caractere | como separador entre os parâmetros. Todos os comandos devem terminar com o caractere #.

```bash

# CREATE
Formato: CREATE|<id>|<marca>|<modelo>|<ano>|<preco>#
Exemplo:
client: CREATE|1|Toyota|Corolla|2020|90000.00#
server: Veículo [id_veiculo] criado com sucesso.

# READ
Formato: READ|<id>#
Exemplo:
client: READ|1#
server: [marca] [modelo] [ano] - [preco]

# READ-ALL
Formato: READ-ALL#
Exemplo:
client: READ-ALL#
server: [lista de veiculos]

# UPDATE
Formato: UPDATE|<id>|<marca>|<modelo>|<ano>|<preco>#
client: UPDATE|1|Honda|Civic|2021|95000.00#
server: Veículo [id_veiculo] atualizado com sucesso.

# DELETE
Formato: DELETE|<id>#
client: DELETE|1#
server: Veículo {id_veiculo} removido com sucesso.

# EXIT
Formato: EXIT#
client: EXIT#
server: Encerrando conexão.
```

## Observações
O sistema não implementa persistência de dados; todos os veículos são mantidos em memória apenas durante a execução do servidor.
O cliente e o servidor usam sockets TCP para se comunicar, com mensagens formatadas manualmente usando o caractere | como delimitador.

