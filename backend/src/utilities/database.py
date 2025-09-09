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

    def has_schema(self, schema_name):
        try:
            self.cursor.execute(f"""SELECT schema_name FROM information_schema.schemata WHERE schema_name='{schema_name}'""")
            if self.cursor.fetchall()==[]:
                return False
            return True

        except Exception as e:
            logger.error(f"Error creating schema: {e}")

    def create_schema(self, schema_name):
        try:
            create_schema_sql = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
            self.cursor.execute(create_schema_sql)
            logger.info(f"Schema '{schema_name}' created successfully.")

        except Exception as e:
            logger.error(f"Error creating schema: {e}")

    def delete_schema(self, schema_name):
        try:
            create_schema_sql = f"DROP SCHEMA IF EXISTS {schema_name} CASCADE;"
            self.cursor.execute(create_schema_sql)
            logger.info(f"Schema '{schema_name}' is removed successfully.")

        except Exception as e:
            logger.error(f"Error creating schema: {e}")

    def create_staging_table_schema(self, in_file, schema_name, table_name) :
        _, extension = os.path.splitext(in_file)
        if extension.strip()==".tsv":
            sep_="\t"
        
        if extension==".csv":
            sep_=","
        
        df = pd.read_csv(in_file, sep=sep_, nrows=0)
        column_schema = ",".join(f'"{col.lower().replace(' ','_')}" TEXT' for col in df.columns)
        create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS  {schema_name}.{table_name} 
            ({column_schema})
        """
        # print(create_table_sql)
        self.cursor.execute(create_table_sql)

    def has_table(self, table_name, schema_name):
        try:
            self.cursor.execute(f"""
                SELECT 
                    table_name
                FROM information_schema.tables
                WHERE table_schema = '{schema_name}' AND table_name = '{table_name}' 
            """)
            if self.cursor.fetchall()==[]:
                return False
            return True

        except Exception as e:
            logger.error(f"Error creating schema: {e}")

    def file_to_table(self, in_file, schema_name, table_name):
        """
            Import CSV file into database
            Parameters:
                db_connection (object): A valid database connection or cursor object.
                table_name (str): The name of the table to import.
                iput_file (str): The path to the input CSV file.
            Returns:
                bool: True if the import is successful
            Raises:
                Exception: If reading from the database or writing to the file fails.
            """
        try:
            root, extension = os.path.splitext(in_file)
            if extension.strip()==".tsv":
                sep_=sql.Literal('\t')
            
            if extension==".csv":
                sep_=sql.Literal(',')

            with open(in_file, 'r') as fh:
                query = sql.SQL(
                        "COPY {schema_name}.{table} FROM STDIN WITH CSV HEADER DELIMITER {delimiter}"
                    ).format(
                        schema_name=sql.Identifier(schema_name),
                        table=sql.Identifier(table_name),
                        delimiter=sep_
                    )
                # print(query)
                self.cursor.copy_expert(query, fh)
      
        except Exception as e:
            logger.error(e)

    
    def load_sql_script(self, sql_file):
        try:
            with open(sql_file, 'r') as f:
                sql_script = f.read()
                self.cursor.execute(sql_script)
        except Exception as e: 
            logger.error(f"Error: {e}")
            raise