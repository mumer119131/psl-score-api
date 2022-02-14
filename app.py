from flask import Flask, jsonify,request
import data_scrape
import all_result
app = Flask(__name__)


@app.route("/", methods=['POST'])
def scarpe():
    data_scrape.data_scrape()
    response = jsonify({"status": "200"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/all-res", methods=['POST'])
def allResult():
    
    if(request.values.get("Body") == "a" or request.values.get("Body") == "A"):
        all_result.all_result()
    else:
        data_scrape.data_scrape()    
    response = jsonify({"status": "200"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)
