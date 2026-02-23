# 🔐 cadastro_mysql

**Sistema de Cadastro e Login com Flask**

Este projeto é uma aplicação web desenvolvida com **Flask (Python)** que implementa um sistema completo de **cadastro, autenticação e gerenciamento de sessões de usuários**, com integração a um **banco de dados MySQL**.

👉 [Acesse o site clicando aqui](https://pedromelo.pythonanywhere.com/)

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

