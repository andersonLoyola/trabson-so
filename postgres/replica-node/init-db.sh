#!/bin/bash
set -e

echo "init database configuration"
psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
 CREATE USER ${DB_REP_USER} WITH REPLICATION LOGIN PASSWORD '${DB_REP_PASS}';
EOSQL
echo "database configuration finished"