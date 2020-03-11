from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    if request.method == 'POST':
        return jsonify(request.json)

# curl --url http://127.0.0.1:5000/ -X POST -H "Content-Type: application/json" --data '{"oid":"12341234"}'