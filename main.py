from flask import Flask, request, render_template,url_for, redirect
from infos import user, host, senha, banco
from database import db
from modelos import Usuario


app = Flask(__name__)    
#Banco de dados:
#conectando ao meu banco local:
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{senha}@{host}/{banco}"
#criando uma variável que represente meu banco de dados:

#definindo que a nossa aplicação flask vai usar esse banco de dados conectado
db.init_app(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/cadastro", methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        primeironome = request.form['primeironome']
        email = request.form['email']
        senha = request.form['senha']
        #criando uma variável que salve todas as infos do usuario - criando uma row onde nome = primeironome (variável que armazenou o nome que o usuário digitou), email = email (digitado pelo usuario) e senha = senha (digitada pelo usuario)
        novo_usuario = Usuario(nome=primeironome, email=email, senha=senha)
        #adicionando na tabela
        db.session.add(novo_usuario)
        #commitando as mudanças
        db.session.commit()
        print(novo_usuario)
        return redirect(url_for('homepage'))
    elif request.method == 'GET':
        return render_template("cadastro.html")

with app.app_context():
    db.create_all()


if __name__  == '__main__':
    app.run(debug=True)



        
    


#main