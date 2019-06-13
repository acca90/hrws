from peewee import DecimalField
from peewee import Model 
from peewee import IntegerField 
from peewee import UUIDField 
from peewee import CharField
from peewee import DateTimeField
from peewee import datetime
from peewee import ForeignKeyField
from commons.database import pg_db
import uuid
  


class Patient(Model):
    uid = UUIDField(column_name='uid')
    name = CharField(column_name='name')

    class Meta:
        database = pg_db 


class Monitoring(Model):
    patient = ForeignKeyField(Patient, column_name='patient')
    begin = DateTimeField(column_name='monitoring_begin',default=datetime.datetime.now)
    end = DateTimeField(column_name='monitoring_end', default=datetime.datetime.now)

    class Meta:
        database = pg_db 

    def __repr__(self):
        return "{},{},{},{}".format(
            str(self.patient.uid),
            str(self.begin),
            str(self.end),
            str(self.indicators)
        )

    @property
    def serialize(self):
        return {
            'patient': str(self.patient.uid),
            'begin': str(self.begin),
            'end': str(self.end),
            'indicators': self.indicators
        }

    @property
    def indicators(self):
        query = Indicator.select().join(Monitoring).where(
            Indicator.monitoring.id == self.id
        )
        return [i.serialize for i in query]

class Indicator(Model):
    indicator = IntegerField(column_name='indicator')
    value =  DecimalField(column_name='value', decimal_places=2)
    monitoring = ForeignKeyField(Monitoring, column_name='monitoring')

    class Meta:
        database = pg_db 

    def __repr__(self):
        return "{},{}".format(
            str(self.indicator),
            str(self.value)
        )

    @property
    def serialize(self):
        return {
            'indicator': str(self.indicator),
            'value': str(round(self.value,2))
        }