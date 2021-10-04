# from flask import Flask
# from flask import Blueprint, render_template


# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template("home.html")
#     # return "Hi Talib"


# # if __name__ == '__main__':
# #     app.run(debug=True)
# #     app.run()

from flask import Flask
from flask import render_template


# print a nice greeting.


# some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service! Append a username
#     to the URL (for example: <code>/Thelonious</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

# add a rule for the index page.


@application.route('/')
def say_hello():
    return render_template("home.html")


# add a rule when the page is accessed with a name appended to the site
# URL.
# run the app.
