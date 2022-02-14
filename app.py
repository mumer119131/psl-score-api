from flask import Flask, jsonify
import data_scrape
app = Flask(__name__)


@app.route("/", methods=['POST'])
def scarpe():
    data_scrape.data_scrape()
    response = jsonify({"status": "200"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)
