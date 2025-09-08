import pandas as pd
import os , logging
from files import download_file_from_link, find_file, tsv_to_csv
from database import DatabaseHandler
from dotenv import load_dotenv
logger = logging.getLogger(__name__)

def build_gene_table(in_file, db_handler):
    # create staging table first, dumping everything from csv to table
    print()
    try:
        db_handler.file_to_staging_table(in_file, schema_name="staging", table_name="genes")
        # create table from schema file
        db_handler.load_sql_script("./resources/db/genes_schema.sql")
        # load data
        db_handler.load_sql_script("./resources/db/genes_load.sql")
    except Exception as e:
        logger.error(f"Error {e}")
        raise

if __name__=="__main__":
    load_dotenv()
    db_databasename = os.getenv("POSTGRES_DB")
    db_host = os.getenv("DB_HOST")
    db_password = os.getenv("DB_PASSWORD")
    db_username = os.getenv("DB_USERNAME")
    db_port = os.getenv("DB_PORT")

    temp_output = "temp"
    os.makedirs(temp_output, exist_ok=True)
    genes_temp_dir = f"{temp_output}/genes"
    if not os.path.exists(genes_temp_dir):
        download_file_from_link("https://api.clinpgx.org/v1/download/file/data/genes.zip", genes_temp_dir)
    
    gene_file = find_file(genes_temp_dir, "genes")
    print(gene_file)
    # tsv_to_csv(gene_file)
    db_handler = DatabaseHandler(db_databasename, db_username, db_password, db_host, db_port)
    build_gene_table(gene_file, db_handler)

