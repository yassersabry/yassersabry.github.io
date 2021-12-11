from flask import Flask

def create_app():
    app = Flask(__name__)
    #secret key for our app
    app.config['SECRET_KEY'] = 'LASKDFLK ASLDKKFJ'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app