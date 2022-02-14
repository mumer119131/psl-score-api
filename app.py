from flask import Flask
import data_scrape
app = Flask(__name__)


@app.route("/")
def scarpe():
    data_scrape.data_scrape()
    return "Done"


if __name__ == "__main__":
    app.run()
