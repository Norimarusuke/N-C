from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/jidou_hanbai")
def jidou_hanbai():
    return render_template("jidou_hanbai.html")

@app.route("/convenience")
def convenience():
    return render_template("convenience.html")

@app.route("/hikageno_basho")
def hikageno_basho():
    return render_template("hikageno_basho.html")

@app.route("/top")
def top():
    return render_template("top.html")

app.run(debug=True, host="0.0.0.0")


