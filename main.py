from flask import Flask, request, json, jsonify
from model import predict

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message='Hello Master of the universe!')


@app.route('/predict', methods=['POST'])
def clasify():
    data = request.get_json()
    print("DATA TYPE:    ", type(data))
    print("--------------------------------------------------------------")
    print(data)
    result = predict(data, 'dist', 'model.pkl')
    return jsonify(result), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug =True)
