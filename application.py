from flask import Flask
from flask import Blueprint, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return "Hi Talib"
    # return render_template("home.html")


# if __name__ == '__main__':
#     app.run(debug=True)
