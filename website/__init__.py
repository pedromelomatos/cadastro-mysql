from flask import Flask
from infos import secretkey

def cria_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretkey
    from .views import views 
    app.register_blueprint(views, url_prefix='/') 
    return app

#__init__