from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World de Dokers un mundo maravislloso! y muchoas otras cosas mas</p>"

print("esto no funciona")
