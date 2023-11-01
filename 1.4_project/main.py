from flask import Flask, request, jsonify

app = Flask(__name__)


# @app.route("/")
# def home():
#     return "Home"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {"user_id": user_id, "name": "Joe", "email": "user_email@example.com"}

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


# "get-user/123?extra=hello world"


@app.route("/create-user", methods=["POST"])
def create_user():
    # if request.method == "POST":
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)

"""
Methods:
GET - retrieve data from source
POST - create a resource
PUT - update a resource
DELETE - delete a resource
"""
