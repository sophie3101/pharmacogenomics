import argparse, os, sys,  configparser
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))) #add the parent directory of the current file to the module search path

from utilities.build_db import build_gene_table
from utilities.database import DatabaseHandler
from utilities.files import download_file_from_link, find_file
from utilities.logger import get_logger
from dotenv import load_dotenv

logger = get_logger(__name__, "app.log")
def build_or_update_database(config):
    load_dotenv()
    db_databasename = os.getenv("POSTGRES_DB")
    db_host = os.getenv("DB_HOST")
    db_password = os.getenv("DB_PASSWORD")
    db_username = os.getenv("DB_USERNAME")
    db_port = os.getenv("DB_PORT")

    temp_output = config.get("DIR","temp_dir")
    logger.info(f"temp dir {temp_output}")
    os.makedirs(temp_output, exist_ok=True)
    genes_temp_dir = f"{temp_output}/genes"

    if not os.path.exists(genes_temp_dir):
        download_file_from_link("https://api.clinpgx.org/v1/download/file/data/genes.zip", genes_temp_dir)
    
    gene_file = find_file(genes_temp_dir, "genes")
    # print(gene_file)
    db_handler = DatabaseHandler(db_databasename, db_username, db_password, db_host, db_port)
    build_gene_table(gene_file, db_handler, config)

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--build_database", action='store_true',help="building postgres database of pgx gene, alleles and drugs")
    parser.parse_args()
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read("backend/config.ini")

    if args.build_database:
        logger.info("BUIDLING DATABASE")
        build_or_update_database(config)
    
    """BUILD CPIC gene """
    print()

if __name__=="__main__":
    main()