#!/bin/bash

echo "Installing pgpool"

if [ ! -d /var/run/pgpool ]; then
    mkdir -p /var/run/pgpool
    chown pgpool:pgpool /var/run/pgpool
fi

PGPOOL_RECOVERY_SQL="./pgpool-recovery.sql"
DATABASE="template1"
export PGPASSWORD='secret'
cd /tmp/pgpool-II-4.5.5 && \
    ./configure && \
    make && \
    make install && \
    cd src/sql/pgpool-recovery  && \
    psql -h "${PRIMARY_NODE_HOST}" -p "${PRIMARY_NODE_PORT}" -d "${DATABASE}" -U postgres -f "${PGPOOL_RECOVERY_SQL}"
echo "PGpool installed successfully"
