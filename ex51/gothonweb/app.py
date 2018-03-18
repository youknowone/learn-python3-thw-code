from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET'])
def index():
    인사말 = "Hello World"

    if request.method == "POST":
        이름 = request.form['name']
        인사 = request.form['greet']
        인사말 = f"{인사}, {이름}"
        return render_template("index.html", 인사말=인사말)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()
