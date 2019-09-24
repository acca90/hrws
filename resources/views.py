from flask_restful import Resource
from resources.models import Patient, Monitoring
from flask import request


class MonitoringView(Resource):
    """
    Class defined for monitoring operations
    """
    def post(self):
        json_request = request.get_json()
        query = Monitoring.select().where(
            Monitoring.begin.between(json_request['begin'], json_request['end'])
        )
        return [monitoring.serialize(True) for monitoring in query]


class PatientView(Resource):
    """
    Class defined for patient operations
    """

    def post(self):
        json_patient = request.get_json()
        records = Patient.select().where(Patient.uuid == json_patient['uuid']).count()
        if records == 0:
            Patient.insert(json_patient).execute()

        return {"success": "Patient correctly recorded"}
