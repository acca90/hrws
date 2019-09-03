from flask_restful import Resource
from resources.models import Patient, Monitoring, Indicator
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
        print(request.get_json())
        return []
