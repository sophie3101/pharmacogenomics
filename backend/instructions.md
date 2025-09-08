1. build database and pgadmin:`docker-compose build up-d` 
To connect to the database: 
    - Using pdadmin (localhost:8080)In pgadmin, connect to dabase:
        host is postgres (container name)
    - Using console:
        `psql -h localhost -p 5433 -U root -d pgx`


2. if want to remove the containers: `docker compose down --volumes`

3. build ` python3 -m venv venv `
 source ./venv/bin/activate