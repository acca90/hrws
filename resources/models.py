from peewee import Model, AutoField, UUIDField, CharField, DateTimeField, datetime, ForeignKeyField
from commons.database import pg_db
import uuid


class Patient(Model):
    id = AutoField(column_name='id', primary_key=True)
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