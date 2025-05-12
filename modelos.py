from database import db
from flask_login import UserMixin #importação que é necessária para o flask entender que a classe é uma classe de login, aí as funções de login passarão a funcionar quando forem buscar ou enviar infos pra essas classe.

#Arquivo Models salva as tabelas do meu banco

#criação de tabela no SQL Alchemy -> classe == tabela:
class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    senha = db.Column(db.String(128), nullable=False)

    #O que a requisição vai retornar no query, nesse caso é o id
    def __repr__(self):
        return f'<{self.nome}>'
    
#models