# 🚀 Deploy no Coolify (VPS)

Este projeto está pronto para ser implantado usando Docker. Siga os passos abaixo para configurar no Coolify.

## Pré-requisitos

1.  Uma VPS (Ubuntu recomendado) com Coolify instalado.
2.  Este repositório acessível pelo Coolify (GitHub público ou privado com chave SSH provisionada).

## Passo a Passo no Coolify

### 1. Criar novo Recurso
No dashboard do seu projeto no Coolify:
1.  Clique em **+ New**.
2.  Selecione **Git Repository** (ou **Public Repository** se for público).
3.  Cole a URL do repositório: `https://github.com/thiagoregueira/flix_api`
4.  Branch: `main`

### 2. Configurações de Build (Build Pack)
O Coolify deve detectar automaticamente, mas certifique-se de selecionar:
*   **Build Pack**: `Docker Compose` ou `Dockerfile`.
*   **Docker Location**: `/Dockerfile` (padrão na raiz).

### 3. Variáveis de Ambiente (Environment Variables)
Vá na aba **Environment Variables** e adicione as chaves de segurança. **Nunca use os valores padrão em produção!**

| Chave | Valor (Exemplo) | Descrição |
| :--- | :--- | :--- |
| `SECRET_KEY` | `sua-chave-secreta-aleatoria-e-longa` | Gere uma nova chave forte. |
| `DEBUG` | `False` | **CRÍTICO**: Deve ser falso em produção. |
| `ALLOWED_HOSTS` | `flixapi.dominio.qzz.io,localhost,127.0.0.1` | Domínios que acessarão a API. |

### 4. Configuração de Domínio
Na aba **General** ou **Configuration**:
*   Defina o **FQDN** (Fully Qualified Domain Name) como: `https://flixapi.dominio.qzz.io`
*   O Coolify cuidará do SSL (HTTPS) automaticamente e gerenciará os redirecionamentos.

### 5. Deploy
Clique em **Deploy**.

O Coolify irá:
1.  Clonar o repo.
2.  Construir a imagem Docker usando o `Dockerfile`.
3.  Rodar o `entrypoint.sh` que aplica migrações e carrega os dados de teste (`initial_data.json`).
4.  Iniciar o Gunicorn na porta 8000.

---

## 🔒 Segurança

*   O container roda com usuário não-root (configurável no Dockerfile se necessário, mas por padrão o Gunicorn gerencia bem).
*   `DEBUG=False` impede vazamento de stack traces.
*   HTTPS é garantido pelo proxy reverso do Coolify (Traefik/Caddy).

## 💾 Banco de Dados

Por padrão, este Dockerfile usa SQLite que será criado dentro do container. **Atenção:** Se você redeployar sem volume persistente, os dados serão perdidos (exceto os do `initial_data.json` que são recarregados).

**Para Persistência (Recomendado):**
No Coolify, configure um **Persistent Storage** (Volume):
*   Monte `/app/db.sqlite3` para um volume local se quiser manter o SQLite.
*   Idealmente, provisione um **PostgreSQL** no Coolify e mude as configurações do `settings.py` para usar Postgres (exige instalar `psycopg2-binary` e alterar `DATABASES`).
