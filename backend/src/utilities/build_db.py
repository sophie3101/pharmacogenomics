import pandas as pd
import os , logging, sys
from utilities.files import download_file_from_link, find_file
from utilities.database import DatabaseHandler
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

def build_gene_table(in_file, db_handler, config):
    # create staging table first, dumping everything from csv to table
    try:
        root_dir = config.get("DIR", "root_dir")
        """STAGING"""
        staging_schema="staging"
        staging_table = "genes"
        stg_schema_script = os.path.join(root_dir, config.get("SQL_SCRIPT", "stg_gene_schema"))
        if not db_handler.has_schema(staging_schema):
            db_handler.create_schema(staging_schema)
        if not db_handler.has_table(staging_table, staging_schema):
            db_handler.load_sql_script(stg_schema_script)
            db_handler.file_to_table( in_file, staging_schema, staging_table)

        """CORE"""
        # create table from schema file
        gene_schema_script=os.path.join(root_dir, config.get("SQL_SCRIPT", "core_gene_schema"))
        db_handler.load_sql_script(gene_schema_script)
        # load data
        gene_load_script=os.path.join(root_dir, config.get("SQL_SCRIPT", "core_gene_loading"))
        db_handler.load_sql_script(gene_load_script)
        logger.info("DONE")
    except Exception as e:
        logger.error(f"Error {e}")
        raise

# if __name__=="__main__":
#     import configparser
#     config = configparser.ConfigParser()
#     config.read("backend/config.ini")
    
#     load_dotenv()
#     db_databasename = os.getenv("POSTGRES_DB")
#     db_host = os.getenv("DB_HOST")
#     db_password = os.getenv("DB_PASSWORD")
#     db_username = os.getenv("DB_USERNAME")
#     db_port = os.getenv("DB_PORT")

#     temp_output = "temp"
#     os.makedirs(temp_output, exist_ok=True)
#     genes_temp_dir = f"{temp_output}/genes"
#     if not os.path.exists(genes_temp_dir):
#         download_file_from_link("https://api.clinpgx.org/v1/download/file/data/genes.zip", genes_temp_dir)
    
#     gene_file = find_file(genes_temp_dir, "genes")
#     print(gene_file)
#     # tsv_to_csv(gene_file)
#     db_handler = DatabaseHandler(db_databasename, db_username, db_password, db_host, db_port)
#     build_gene_table(gene_file, db_handler,config)

