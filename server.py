import os
from flask import Flask, send_from_directory
import api

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.','index.html')

@app.route('/api/lists', methods=['GET'])
def get_lists():
    return api.get_lists()

@app.route('/api/trends', methods=['GET'])
def get_trend_concepts():
    return api.get_trending_concepts()

@app.route('/api', methods=['GET'])
def startpage():
    return "Hi!"

@app.route('/api/meta', methods=['GET'])
def metadata():
    return api.metadata()

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
