import argparse, os, sys,  configparser, subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))) #add the parent directory of the current file to the module search path

from utilities.files import download_gz_file
from utilities.logger import get_logger
from dotenv import load_dotenv

logger = get_logger(__name__, "app.log")


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--build_database", action='store_true',help="building postgres database of pgx gene, alleles and drugs")
    parser.parse_args()
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read("backend/config.ini")

    if args.build_database:
        logger.info("BUIDLING DATABASE")
        
        db_databasename = os.getenv("POSTGRES_DB")
        db_host = os.getenv("DB_HOST")
        db_password = os.getenv("DB_PASSWORD")
        db_username = os.getenv("DB_USERNAME")
        db_port = os.getenv("DB_PORT")
        # db_handler = DatabaseHandler(db_databasename, db_username, db_password, db_host, db_port)
        # if db_handler.has_schema('cpic'):
        #     user_input = input("")
        db_link = config.get("LINK", "db_link")
        uncompressed_bytes = download_gz_file(db_link)
        cmd = ['psql', f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_databasename}"]
        logger.info(f"copy cpic database into {db_databasename}.cpic")
        result=subprocess.run(cmd, input=uncompressed_bytes, capture_output=True)
        logger.info(result.stdout)
        logger.error(result.stderr)


if __name__=="__main__":
    main()