from playhouse.postgres_ext import PostgresqlExtDatabase


pg_db = PostgresqlExtDatabase(
    'monitoramento', 
    user='postgres', 
    password='f1234',
    host='localhost', 
    port=5432
)