from flask import Flask, request, render_template,url_for, redirect, flash
from infos import user, host, senha, banco, secretkey
from database import db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from modelos import Usuario
import hashlib


app = Flask(__name__)    
app.secret_key = secretkey
#sistema responsável pelo gerenciamento do login na nossa aplicação
lm = LoginManager(app)
#Banco de dados:
#conectando ao meu banco local:
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{senha}@{host}/{banco}"
#criando uma variável que represente meu banco de dados:

#definindo que a nossa aplicação flask vai usar esse banco de dados conectado
db.init_app(app)

#função pra criptografar a senha quando ela for enviada pro banco de dados
def hash(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()

lm.login_view = '/'

@lm.user_loader
def user_loader(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method=='POST':
        #LOGIN:
        email= request.form['email']
        senha=hash(request.form['senha'])
        #procurando no banco de dados se tem um usuário com esse email e senha
        usuario_db = db.session.query(Usuario).filter_by(email=email, senha=senha).first()  
        #se não encontrar ninguém registrado com esse email e senha:
        if not usuario_db:
            return render_template("invalido.html")
        #agora se as infos de login foram encontrados na base de dados:
        login_user(usuario_db) #logando o usuário
        return redirect(url_for('bemvindo'))
    

@app.route("/perfil")
@login_required #só entra em /perfil quem estiver logado, que é feito pela função login_user()
def bemvindo():
    nome = current_user.nome
    email = current_user.email
    senha = current_user.senha
    return render_template('infos.html', nome=nome, email=email, senha=senha)

@app.route("/cadastro", methods=['GET','POST'])
def cadastro():
    if request.method == 'GET':
        return render_template("cadastro.html")
    elif request.method == 'POST':
        primeironome = request.form['primeironome']
        email = request.form['email']
        senha = request.form['senha']
        #criando uma variável que salve todas as infos do usuario - criando uma row onde nome = primeironome (variável que armazenou o nome que o usuário digitou), email = email (digitado pelo usuario) e senha = senha (digitada pelo usuario)
        novo_usuario = Usuario(nome=primeironome, email=email, senha=hash(senha))
        #adicionando na tabela
        db.session.add(novo_usuario)
        #commitando as mudanças
        db.session.commit()
        login_user(novo_usuario)
        print(novo_usuario)
        return redirect(url_for('bemvindo'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

with app.app_context():
    db.create_all()


if __name__  == '__main__':
    app.run(debug=True)



        
    


#main