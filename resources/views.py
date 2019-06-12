from flask_restful import Resource
from resources.models import Patient, Monitoring


class MonitoringView(Resource):

    def get(self):

        monitorings = Monitoring.select()
        monitorings_array = []

        for monitoring in monitorings:
            monitorings_array.append({
                'patient': str(monitoring.patient.uid),
                'begin': str(monitoring.begin),
                'end': str(monitoring.end)
            })

        return monitorings_array
    
