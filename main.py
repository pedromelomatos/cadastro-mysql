from website import cria_app
from website import views
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from infos import user, host, senha, banco



app = cria_app()

#Banco de dados:
#conectando ao meu banco local:
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{senha}@{host}/{banco}"
#criando uma variável que represente meu banco de dados:
db = SQLAlchemy()

db.init_app(app)

#criação de tabela no SQL Alchemy -> classe == tabela:
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)

    #O que a requisição vai retornar no query, nesse caso é o id
    def __repr__(self):
        return f'<{self.nome}>'

with app.app_context():
    #fazendo uma requisição na tabela de usuários
    usuario = db.session.query(Usuario).filter_by(email='hannah@email.com').first()
    #deletando a row onde o email é hannah@email.com
    db.session.delete(usuario)
    db.session.commit()


if __name__  == '__main__':
    app.run(debug=True)


#main