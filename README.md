# cep-consult-netip

Este repositório contém uma API para consulta de existência de CEP em uma determinada collection no MongoDB.

## Instruções de uso

Inserir a URI de conexão é o banco de dados à ser utilizado no arquivo `.env`

Executar o comando `docker compose up -d` para executar.

O serviço é executado utilizado a porta 5000.
Se necessário, alterar a porta no arquivo `docker-compose.yml`

```
    ports: 
     - PORTA:5000
```
