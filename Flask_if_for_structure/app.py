
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first = "dello delilo destane bu benim ilk conditione"
    return render_template("index.html", message=first)

@app.route('/Adem')
def mylist():
    names = ["ahmet arif", "salih", "tarkan", "sergio", "halil"]
    return render_template("body.html", object = names)


if __name__=="__main__":
   # app.run(debug=True,port=2000) 
    app.run(host = '0.0.0.0', port = 80)