#!/bin/bash

docker exec -i oragriculture_postgres_1 psql -U postgres -c "CREATE DATABASE agtech"
docker exec -i oragriculture_postgres_1 psql -U postgres -c "CREATE DATABASE alex"
docker exec -i oragriculture_postgres_1 psql -U postgres -c "CREATE USER alex WITH CREATEUSER"
docker exec -i oragriculture_postgres_1 psql -U postgres -c "ALTER USER alex WITH PASSWORD 'mysecretpassword'"

if [ -f backup-or-agriculture-oct-22-2015.sql.gz ]; then
  gunzip backup-or-agriculture-oct-22-2015.sql.gz
fi
docker exec -i oragriculture_postgres_1 psql -U postgres agtech < backup-or-agriculture-oct-22-2015.sql 
