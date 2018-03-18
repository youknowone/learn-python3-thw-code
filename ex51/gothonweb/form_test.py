from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
    이름 = request.args.get('name', '아무개')

    if 이름:
        인사말 = f"안녕, {이름}"
    else:
        인사말 = "Hello World"

    return render_template("index.html", 인사말=인사말)

if __name__ == "__main__":
    app.run()
