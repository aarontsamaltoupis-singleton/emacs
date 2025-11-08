
flask
from flask import Flask



app = Flask(__name__) ## 

@app.route("/")
@app.route("/<>")

##this sets the url of the page, which in this case would be http://localhost:5000/hello

def hello_world():
    return("hellllllo world")


if __name__ == "__main__":
    app.run()



dynamic route:

change @app.route to :

@app.route("/tesst/<search_query>")
-the url of the webpage is now tesst/ followed by whatever the user enters which is saved as the variable <search_query>

if this variable is incorporated into a function it can be printed on the page:

def search(search_query):
 return(search_query)

# different types in URLs








# response tuples

each value that is returned to the webpage is actually a tuple consisting of the actual response, the status of the response and the headers

the response would be the actual text written, the status could be 404 for an error message (the default is 200) and the headers text/html in this example.

the status can be set like this: 
@app.route("/text")
def returning():
 return("response", 404) 

 404 here is the status



# Debug mode
enabling debug:
add
app.config["DEBUG"] = True

to app.py after creating the app object


this also enables auto refresh












blog.py

##CONTROLLER


# imports

from flask import Flask, render_template, request, session, flash, redirect, url_for, g

import sqlite3


# configuration

DATABASE = "blog.db"

app = Flask(__name__)


app.config.from_object(__name__)


# defining function used to connect to the database
def connectdb():
    return sqlite3.connect(app.config["DATABASE"])


if __name__ == '__main__':
    app.run(debug =True)
