import datetime
import json
from flask import Flask, jsonify

app = Flask(__name__)

def log_to_file(obj):
    open('logs.txt', 'a').write(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " | " + json.dumps(obj) + '\n'
    )


@app.route('/showAll')
def show_all():
    obj = {"message":"OK"}
    print(str(obj))
    log_to_file(obj)
    return jsonify(obj)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=30001)
    # app.run(debug=False)