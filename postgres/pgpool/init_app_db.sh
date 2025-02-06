export PGPASSWORD='secret'
if psql -h ${PRIMARY_NODE_HOST} -p ${PRIMARY_NODE_PORT} -U "postgres" -c "SELECT 1 FROM pg_database WHERE datname = '$DATABASE_APP_NAME';" | grep -q 1; then
    echo "Database $DATABASE_APP_NAME exists. Skipping DB application initialization."
else
psql -h ${PRIMARY_NODE_HOST} -p ${PRIMARY_NODE_PORT} -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE ROLE ${DB_APP_USER} WITH LOGIN CREATEDB PASSWORD '${DB_APP_PASSWORD}';
    CREATE DATABASE ${DATABASE_APP_NAME} OWNER ${DB_APP_USER};
EOSQL
fi
echo "${DB_APP_USER}:${DB_APP_PASSWORD}" >> /usr/local/etc/pool_passwd
unset $PGPASSWORD    