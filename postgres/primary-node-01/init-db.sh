#!/bin/bash
set -e
echo "Creating replication users"
psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE USER ${DB_REP_USER} WITH REPLICATION LOGIN SUPERUSER ENCRYPTED PASSWORD '${DB_REP_PASS}';
    CREATE DATABASE repmgr OWNER ${DB_REP_USER};
EOSQL