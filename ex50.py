from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    인사말 = "World"
    return f'Hello, {인사말}!'

if __name__ == "__main__":
    app.run()

