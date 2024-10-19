from flask import Flask

app = Flask(__name__) #__name__ is always unique

@app.route('/')
def home():
    return "Hello, uwu!"


if __name__ == "__main__":
    app.run(debug=True)