from flask import render_template
from flask import Blueprint

views = Blueprint('views', __name__)

#Rotas do site

@views.route("/")
def homepage():
    return render_template("index.html")

@views.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

#views