from flask import Flask
from flask import render_template


application = Flask(__name__)
if __name__ == "__main__":
    application.debug = True
    application.run()


@application.route('/')
def say_hello():
    return render_template("home.html")
