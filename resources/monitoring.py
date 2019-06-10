from flask_restful import Resource


class HeartRateWebService(Resource):
    def post(self):
        return {'hello': 'post'}
    
