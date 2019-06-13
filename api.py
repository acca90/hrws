from flask import Flask
from resources.views import MonitoringView
from flask_restful import Api

api_version = '/api/v1/'
app = Flask(__name__)
api = Api(app, catch_all_404s=True)


api.add_resource(MonitoringView, api_version + 'monitoring')


if __name__ == '__main__':
    app.run(debug=True)



