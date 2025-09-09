1. build database and pgadmin:`docker-compose up -d` 
To connect to the database: 
    - Using pdadmin (localhost:8080)In pgadmin, connect to dabase:
        host is postgres (container name)
    - Using console:
        `psql -h localhost -p 5433 -U root -d pgx`
        using docker:
        `docker exec -it postgres psql -U root -d pgx`

2. if want to remove the containers: `docker compose down --volumes`

3. build ` python3 -m venv venv `
 source ./venv/bin/activate

 4. to test using pgtap alone, still not working
  docker exec -it postgres psql -U root -d pgx -c 'CREATE EXTENSION IF NOT EXISTS pgtap;'
 docker exec -it postgres psql -U root -d pgx < pgtap.sql 
 or 
 psql -h localhost -p 5433 -U root -d pgx < pgtap.sql 

5. to do unit tests: pytest 
or if want to test specifically file: pytest -s <filename>


use https://www.clinpgx.org/downloads
genes table: from https://api.clinpgx.org/v1/download/file/data/genes.zip

note: i found out the the cpic github has released a full database sql file : 
https://github.com/cpicpgx/cpic-data/releases (looking for Full DB export available)
on sep 8, the recent one is https://files.cpicpgx.org/data/database/cpic_db_dump-v1.51.0.sql.gz