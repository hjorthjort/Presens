import os
from flask import Flask
import api

app = Flask(__name__)

@app.route('/api/lists', methods=['GET'])
def get_lists():
    return api.get_lists()


@app.route('/api', methods=['GET'])
def index():
    return "Hi!"


port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
