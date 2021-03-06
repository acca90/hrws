import json
from peewee import DecimalField
from peewee import Model
from peewee import IntegerField
from peewee import UUIDField
from peewee import CharField
from peewee import DateTimeField
from peewee import datetime
from peewee import ForeignKeyField
from commons.database import pg_db


class Patient(Model):
    """
    Model that represents the patient
    """
    uuid = UUIDField(column_name='uuid')
    first_name = CharField(column_name='first_name')
    last_name = CharField(column_name='last_name')
    birth_date = DateTimeField(column_name='birth_date')
    gender = IntegerField(column_name='gender')

    class Meta:
        database = pg_db

    def serialize_reference(self):
        return {
            'uuid': str(self.uuid),
            'name': str(self.first_name) + " " + str(self.last_name),
            'origin': "localhost:5000" # TODO MELHORAR
        }


class Monitoring(Model):
    """
    Model that represents the monitoring period 
    """
    uuid = UUIDField(column_name='uuid')
    patient = ForeignKeyField(Patient, column_name='patient')
    begin = DateTimeField(column_name='monitoring_begin', default=datetime.datetime.now)
    end = DateTimeField(column_name='monitoring_end', default=datetime.datetime.now)

    class Meta:
        database = pg_db

    def __repr__(self):
        return "{},{},{},{},{}".format(
            str(self.patient.uuid),
            str(self.uuid),
            str(self.begin),
            str(self.end),
            str(self.indicators)
        )

    def serialize(self, eager=False):
        return {
            'uuid': str(self.uuid),
            'reference': str(self.patient.uuid),
            'begin': str(self.begin),
            'end': str(self.end),
            'indicators': self.indicators() if eager else []
        }

    def indicators(self):
        query = Indicator.select().join(Monitoring).where(
            Indicator.monitoring.id == self.id
        )
        return [i.serialize() for i in query]


class Indicator(Model):
    """
    Model that represents sleep quality indicators
    """
    indicator = IntegerField(column_name='indicator')
    value = DecimalField(column_name='value', decimal_places=2)
    monitoring = ForeignKeyField(Monitoring, column_name='monitoring')

    class Meta:
        database = pg_db

    def __repr__(self):
        return "{},{}".format(
            str(self.indicator),
            str(self.value)
        )

    def serialize(self):
        return {
            'indicator': str(self.indicator),
            'value': str(round(self.value, 2))
        }
