from crawler import crawler
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/v1', methods=['POST'])
def post():
    try:
        crawler()
        data = {
            "response": "ok"
        }
    except Exception as e:
        data = {
            "response": f"Error:{e}"
        }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)