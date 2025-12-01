# Projeto FastAPI - CRUD de Clientes, Produtos e Pedidos

Este é um projeto simples de API desenvolvido em **FastAPI** para fins acadêmicos.  
O projeto implementa um **CRUD** (Create, Read, Update, Delete) para **Clientes**, **Produtos** e **Pedidos**.

---

## Tecnologias Utilizadas

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite (banco de dados local)
- Pydantic (validação de dados)

---

## Estrutura do Projeto

- `main.py` - arquivo principal que inicializa a aplicação.
- `models/` - definição das tabelas (Clientes, Produtos, Pedidos).
- `migrations/` - migrações do banco de dados.
- `schemas/` - schemas do Pydantic para validação de dados.
- `services/` - funções CRUD para cada entidade (serviços que interagem com o banco).
- `controllers/` - onde os endpoints são definidos e os serviços (`services/`) são chamados. Cada controller é responsável por receber a requisição, chamar a função apropriada do CRUD e retornar a resposta.
- `database.py` - configuração da conexão com o banco.
- `.env` - arquivo de configuração de ambiente (não enviado por segurança).
- `.env_example` - exemplo de arquivo de configuração de ambiente.


---

## Configuração do Ambiente

1. **Clonar o projeto**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_PROJETO>

2. **Criar ambiente virtual e instalar dependências**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux / Mac
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt

3. **Configurar variáveis de ambiente**:
   ```bash
    O projeto utiliza um arquivo .env para armazenar configurações sensíveis e do banco de dados.
    Para começar a utilizar o projeto, precisa ser criado um arquivo .env na raiz do projeto.
    Para facilitar, copie o arquivo .env_example para .env:

4. **Rodando a Aplicação**:
    ```bash
    Para iniciar a API, rode:
    uvicorn main:app --reload

    A API estará disponível em: http://127.0.0.1:8000 ou localhost:8000

    O FastAPI gera um Swagger automaticamnete, uma documentação, que está disponível em: http://127.0.0.1:8000/docs ou localhost:8000/docs

5. **Endpoints Disponíveis**:
    ```
    Login

    POST /login - Realiza login do cliente (Utilize o email do cliente teste cadastrado: cliente@email.com e a senha: 123)

    GET /me - Retorna os dados do usuário autenticado (Endpoint autenticado)

    ----------------------------------------------

    Clientes

    GET /clientes - Listar todos os clientes

    GET /clientes/{id} - Buscar cliente por ID

    POST /clientes - Criar novo cliente

    PUT /clientes/{id} - Atualizar cliente

    DELETE /clientes/{id} - Deletar cliente (soft delete)

    DELETE /clientes/{id} - Deletar cliente (hard delete, deleta permanentemente)

    ----------------------------------------------

    Produtos

    GET /produtos - Listar todos os produtos

    GET /produtos/{id} - Buscar produto por ID

    POST /produtos - Criar novo produto

    PUT /produtos/{id} - Atualizar produto

    DELETE /produtos/{id} - Deletar produto (soft delete)

    DELETE /produtos/{id} - Deletar produto (hard delete, deleta permanentemente)

    ----------------------------------------------

    Pedidos

    GET /pedidos - Listar todos os pedidos

    GET /pedidos/{id} - Buscar produto por ID

    POST /pedidos - Criar novo pedido (Na hora de criar pedido, não passar o "pedido_id", pode apagar essa linha do json)

    PUT /pedidos/{id} - Atualizar pedido 

    DELETE /pedidos/{id} - Deletar pedido (soft delete)

    DELETE /pedidos/{id} - Deletar pedido (hard delete, deleta permanetemente)