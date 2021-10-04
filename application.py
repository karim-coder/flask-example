from flask import Blueprint, render_template
from flask import Flask
# from website import create_app


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my secret key'

    app.register_blueprint(views, url_profix='/')

    return app

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
