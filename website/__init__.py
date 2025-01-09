from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'callan'

    from .views import views
    from .sal_func import avg_sal

    app.register_blueprint(views, url_prefix= "/")
    
    return app