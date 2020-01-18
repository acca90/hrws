from flask import Flask
from resources.views import MonitoringView, PatientView, generate_and_send_patient
from flask_restful import Api

api_version = '/api/v1/'
app = Flask(__name__)
api = Api(app, catch_all_404s=True)


@app.route('/')
def main():
    return "HRWS it's working"


@app.route('/send')
def send():
    generate_and_send_patient()
    return "Sending patients"


api.add_resource(MonitoringView, api_version + 'monitoring')
api.add_resource(PatientView, api_version + 'patient')

if __name__ == '__main__':
    app.run(debug=True)
