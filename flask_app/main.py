import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello World!</h1>'


users = [
    {
        "name": "Dima",
        "messege": "Hello",
    }, {
        "name": "Kira",
        "messege": "Hi",
    }
]


@app.route("/user/<name>")
def user(name):
    return '<h1>Hi, %s!</h1>' % name


@app.route("/users/", methods=["POST"])
def added_user():
    data = request.get_json()
    users.append(data[0])
    print(data)
    return data


@app.route("/users/", methods=["GET"])
def get_all_users():
    return json.dumps(users)


if __name__ == '__main__':
    app.run(debug=True)
