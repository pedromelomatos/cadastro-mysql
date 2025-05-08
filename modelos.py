from database import db

#Arquivo Models salva as tabelas do meu banco

#criação de tabela no SQL Alchemy -> classe == tabela:
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    senha = db.Column(db.String(128), nullable=False)

    #O que a requisição vai retornar no query, nesse caso é o id
    def __repr__(self):
        return f'<{self.nome}>'