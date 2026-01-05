# 🔐 cadastro_mysql

**Sistema de Cadastro e Login com Flask**

Este projeto é uma aplicação web desenvolvida com **Flask (Python)** que implementa um sistema completo de **cadastro, autenticação e gerenciamento de sessões de usuários**, com integração a um **banco de dados MySQL**.

---

## 🛠️ Funcionalidades

* 🔹 Cadastro de novos usuários com nome, email e senha
* 🔹 Criptografia de senhas com **SHA-256** antes de armazenar no banco
* 🔹 Login com verificação de credenciais
* 🔹 Sessão autenticada com **Flask-Login**
* 🔹 Proteção de rotas: acesso a páginas privadas somente para usuários logados
* 🔹 Logout com destruição segura da sessão
* 🔹 Armazenamento de dados com **SQLAlchemy** e conexão ao banco via variáveis de ambiente

---

## 💡 Tecnologias utilizadas

* 🔹 **Flask** (framework web)
* 🔹 **Flask-Login** (gerenciamento de sessões)
* 🔹 **SQLAlchemy** (ORM)
* 🔹 **MySQL** com **PyMySQL**
* 🔹 **Hashlib** (criptografia de senha)
* 🔹 **HTML + Jinja2** para os templates

---

## 🌐 Estrutura básica

* 🔹 `index.html`: página inicial e de login
* 🔹 `cadastro.html`: formulário de registro
* 🔹 `infos.html`: página protegida com dados do usuário logado
* 🔹 `invalido.html`: página exibida em caso de falha no login
* 🔹 `database.py`: configuração do SQLAlchemy
* 🔹 `modelos.py`: definição do modelo `Usuario`

---

## ▶️ Como executar o projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/pedromelomatos/cadastro-mysql.git
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:

   ```text
   DB_USER
   DB_PASSWORD
   DB_HOST
   DB_NAME
   SECRET_KEY
   ```

5. Execute a aplicação:

   ```bash
   python main.py
   ```
