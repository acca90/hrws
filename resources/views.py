from flask import request
from flask_restful import Resource
from resources.models import Patient, Monitoring
from commons.database import pg_db
import requests
import socket


class MonitoringView(Resource):
    """
    Class defined for monitoring operations
    """
    def post(self):
        """
        Handle's post request for monitorings
        """
        if 'patients' in request.get_json():
            return self.fetch_by_patients(request.get_json())

        return self.fetch_all(request.get_json())

    def fetch_by_patients(self, json_request):
        """
        Fetch monitoring results filtering by patients
        """
        return None

    def fetch_all(self, json_request):
        """
        Fetch all monitoring results
        """
        query = Monitoring.select().where(
            Monitoring.begin.between(json_request['begin'], json_request['end'])
        )
        return [monitoring.serialize(True) for monitoring in query]


class PatientView(Resource):
    """
    Class defined for patient operations
    """

    def post(self):

        print(request.get_json())

        """
        json_patient = request.get_json()
        records = Patient.select().where(Patient.uuid == json_patient['uuid']).count()
        if records == 0:
            Patient.insert(json_patient).execute(pg_db)

        """
        return {"success": "Patient correctly recorded"}



def generate_and_send_patient():
    """
    Method defined to generate and send patient reference for sleepweb 
    this is a conceptual method for validation, not standard
    """
    patients = Patient.select().execute(pg_db)
    for patient in patients:
        requests.post(
            url="http://localhost:8000/api/v1/patient/remote/",
            data=patient.serialize_reference()
        )
