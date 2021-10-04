from flask import Flask
from flask import Blueprint, render_template


# application = Flask(__name__)


# @application.route('/')
# def hello_world():
#     return 'Hello there!'
app = Flask(__name__)
# def create_app():
#     app.config['SECRET_KEY'] = 'my secret key'

#     app.register_blueprint(views, url_profix='/')

#     return app


# views = Blueprint('views', __name__)


@app.route('/')
def home():
    return render_template("home.html")


# app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
