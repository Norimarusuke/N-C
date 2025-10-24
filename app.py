from flask import Flask, render_template,redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("/top")

@app.route("/jidou_hanbai")
def jidou_hanbai():
    return render_template("jidou_hanbai.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

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

@app.route("/call3")
def call3():
    return render_template("call3.html")

@app.route("/kion")
def kion():
    import requests
    API_KEY = "0ea8fd21d3e847189e5b6a088b5f248f"
    url = f"https://api.weatherbit.io/v2.0/current?lat=39.68809830869338&lon=141.16449176101054&lang=ja&units=M&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(data["data"][0]["app_temp"])
    kion = data["data"][0]["app_temp"]
    print(data["data"][0]["rh"])
    rh = data["data"][0]["rh"]
    kiken = "危険"
    gazou = "/static/呪いちゃん.png"
    if kion < 5:
        kiken = "激さむゥ"
        gazou = "/static/呪いちゃん.png"
    if kion < 28:
        kiken = "安全"
        gazou = "/static/喜びちゃん.jpg"
    if kion > 28:
        kiken = "注意"
        gazou = "/static/怒りさん.jpg"
    if kion > 32:
        kiken = "危険"
        gazou = "/static/汗だくちゃん.jpg"
    return render_template("kion.html", kion=kion, rh=rh, kiken=kiken, gazou=gazou)



@app.route("/おためし")
def おためし():
    namae = "ゆうまる"
    namae2 = "れいまる"
    return render_template("おためし.html" ,abc=namae ,aaa=namae2) 

app.run(debug=True, host="0.0.0.0")


