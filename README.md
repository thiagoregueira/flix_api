
# 🎬 Flix API - Gerenciamento de Filmes e Críticas

Aplicação REST API desenvolvida em Django com Django Rest Framework (DRF) para gerenciamento completo de um catálogo de filmes, atores, gêneros e avaliações.

## 🚀 Sobre o Projeto

A **Flix API** permite que usuários se cadastrem, e interajam com um banco de dados de filmes. O sistema conta com autenticação JWT, permissões de acesso granulares e uma documentação interativa completa.

### Principais Recursos
*   **Autenticação JWT**: Segurança robusta para acesso aos endpoints.
*   **CRUD Completo**: Gestão de Filmes, Atores, Gêneros e Avaliações.
*   **Estatísticas**: Endpoints dedicados para análise de dados do catálogo.
*   **Documentação Interativa**: Swagger UI e Redoc integrados via OpenAPI 3.0.
*   **Permissões**: Controle de acesso (apenas usuários autenticados).

---

## 🛠 Tecnologias Utilizadas

*   **Python 3.12+**
*   **Django 5.2**
*   **Django Rest Framework (DRF)** 3.16
*   **Simple JWT** (Autenticação)
*   **drf-spectacular** (Documentação OpenAPI 3.0)
*   **SQLite** (Banco de dados padrão)

---

## ⚙️ Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clonar o repositório
```bash
git clone https://github.com/thiagoregueira/flix_api.git
cd flix-api
```

### 2. Criar e ativar o ambiente virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Aplicar migrações
Crie o banco de dados e as tabelas necessárias:
```bash
python manage.py migrate
```

### 5. Carregar dados iniciais (Opcional)
Para popular o banco com filmes, gêneros e usuários de demonstração:
```bash
python manage.py loaddata initial_data.json
```

### 5. Criar superusuário (Opcional)
Para acessar o admin do Django:
```bash
python manage.py createsuperuser
```

### 6. Executar o servidor
```bash
python manage.py runserver
```
Acesse a API em: `http://127.0.0.1:8000/`

---

## 📚 Documentação da API (Swagger UI)

A documentação completa e interativa pode ser acessada em:
👉 **[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)**

Lá você encontrará todos os endpoints detalhados, exemplos de requisição/resposta e poderá testar as rotas diretamente pelo navegador.

Alternativa (Redoc): `http://127.0.0.1:8000/api/schema/redoc/`

---

## 🔐 Autenticação e Teste Rápido

A API utiliza autenticação via Token JWT. Para acessar os endpoints protegidos, você precisa obter um token `access`.

### Usuário de Teste (Exemplo)
Você pode usar as credenciais abaixo para testar a API (já configurados em produção):

| Campo | Valor | Observação |
| :--- | :--- | :--- |
| **Username** | `usuarioteste` | Usuário comum para consumo da API |
| **Password** | `@123456@` | |
| **Username** | `admin` | Superusuário (Painel Administrativo) |
| **Password** | `admin123` | Acesso total ao sistema |

### Passo a passo para autenticar no Swagger:
1.  Acesse o endpoint `POST /api/v1/authentication/token/` no Swagger.
2.  Envie o JSON com as credenciais acima.
3.  Copie o token `access` retornado.
4.  Clique no botão **Authorize** (cadeado) no topo da página.
5.  Cole o token no formato: `Bearer SEU_TOKEN_AQUI`.
6.  Clique em **Authorize** e pronto! Agora você pode testar rotas como `/api/v1/movies/`.

---

## 🛣 Principais Endpoints

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/api/v1/authentication/token/` | Login (Obter Access e Refresh Token) |
| `GET` | `/api/v1/movies/` | Listar todos os filmes |
| `POST` | `/api/v1/movies/` | Cadastrar novo filme |
| `GET` | `/api/v1/movies/stats/` | Estatísticas gerais do catálogo |
| `GET` | `/api/v1/genres/` | Listar gêneros |
| `GET` | `/api/v1/actors/` | Listar atores |
| `POST` | `/api/v1/reviews/` | Avaliar um filme |

---

## 📞 Contato

Dúvidas ou sugestões? Entre em contato!

---
*Desenvolvido com ❤️ usando Django e DRF.*
