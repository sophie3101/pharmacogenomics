import psycopg2, logging, os
from psycopg2 import sql
import pandas as pd 

logger = logging.getLogger(__name__)
class DatabaseHandler():
    def __init__(self, database_name, username, password, host, port) :
        try:
            self.conn = psycopg2.connect(
                dbname=database_name,
                user = username,
                password = password,
                host = host,
                port = port
            )
            self.conn.autocommit = True
            self.cursor=self.conn.cursor()
            logger.info(f"Successfully connected to the PostgreSQL database {database_name}!")

        except Exception as e:
            logger.error(e)
            raise Exception

    def load_sql_script(self, sql_file):
        try:
            with open(sql_file, 'r') as f:
                sql_script = f.read()
                self.cursor.execute(sql_script)
        except Exception as e: 
            logger.error(f"Error: {e}")
            raise
        
    def has_schema(self, schema_name):
        try:
            self.cursor.execute(f"""SELECT schema_name FROM information_schema.schemata WHERE schema_name='{schema_name}'""")
            if self.cursor.fetchall()==[]:
                return False
            return True

        except Exception as e:
            logger.error(f"Error creating schema: {e}")