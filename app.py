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

@app.route("/call")
def call():
    return render_template("call.html")

@app.route("/call2")
def call2():
    return render_template("call2.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/house")
def house():
    return render_template("house.html")

@app.route("/drink")
def drink():
    return render_template("drink.html")

@app.route("/house2")
def house2():
    return render_template("house2.html")

@app.route("/house3")
def house3():
    return render_template("house3.html")

@app.route("/house4")
def house4():
    return render_template("house4.html")



@app.route("/おためし")
def おためし():
    namae = "ゆうまる"
    namae2 = "れいまる"
    return render_template("おためし.html" ,abc=namae ,aaa=namae2) 

app.run(debug=True, host="0.0.0.0")


