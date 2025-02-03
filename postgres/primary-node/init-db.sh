#!/bin/bash
set -e
echo "Creating user: ${DB_REP_USER} with password ${DB_REP_PASS}"
psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE USER ${DB_REP_USER} WITH REPLICATION LOGIN PASSWORD '${DB_REP_PASS}';
EOSQL