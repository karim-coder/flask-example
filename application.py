from flask import Flask

application = Flask(__name__)


@application.route('/')
def home():
    return "Hi Talib"
    # return render_template("home.html")


# if __name__ == '__main__':
#     app.run(debug=True)
