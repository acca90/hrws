from flask import Flask
from resources.monitoring import HeartRateWebService
from flask_restful import Api

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

api.add_resource(HeartRateWebService, '/api/v1/async')


if __name__ == '__main__':
    app.run(debug=True)



