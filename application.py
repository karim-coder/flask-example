from flask import Flask
from flask import Blueprint, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")
    # return "Hi Talib"


# if __name__ == '__main__':
#     app.run(debug=True)
#     app.run()
