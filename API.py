from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_all():
    print("Hello")
    return "1"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)