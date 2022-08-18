from flask import Flask, request, jsonify, Response


# ? Creating app with Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print("triggered ... ")
    key = request.args.get("key")
    print(key)
    # return Response("Hello World !", status=200, mimetype='application/json')v
    data = {"status": "success", "some key": "some value"}
    return 200


