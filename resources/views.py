from flask_restful import Resource
from resources.models import Patient, Monitoring
from flask import request


class MonitoringView(Resource):
    """
    Class defined for monitoring operations
    """

    def post(self):
        query = Monitoring.select().where(
            Monitoring.begin.between(request.form['begin'], request.form['end'])
        )
        return [monitoring.serialize(True) for monitoring in query]


class PatientView(Resource):
    """
    Class defined for patient operations
    """

    def post(self):
        patient = request.get_json()
        records = Patient.select().where(Patient.uuid == patient['uuid']).count()
        if records == 0:
            Patient.insert(patient).execute()

        return {"success": "Patient correctly recorded"}
