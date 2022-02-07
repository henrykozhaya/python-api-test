from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_all():
    print("Hello")
    return "1"


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8000)
    # app.run(debug=False)