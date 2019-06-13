from flask_restful import Resource
from resources.models import Patient, Monitoring, Indicator


class MonitoringView(Resource):

    def get(self):
        query = Monitoring.select().where(
            Monitoring.begin.between('2019-01-17 00:00:00', '2019-01-17 11:58:00')
        )
        return [monitoring.serialize for monitoring in query]

 
    
