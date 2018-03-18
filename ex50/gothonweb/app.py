from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    인사말 = "Hello, World!"
    return render_template("index.html", 인사말=인사말)

if __name__ == "__main__":
    app.run()

