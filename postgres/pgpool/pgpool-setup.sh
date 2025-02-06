#!/bin/bash

if [ ! -d /var/run/pgpool ]; then
    mkdir -p /var/run/pgpool
    chown pgpool:pgpool /var/run/pgpool
fi

PGPOOL_RECOVERY_SQL="./pgpool-recovery.sql"
DATABASE="template1"
export PGPASSWORD='secret'
echo "Installing pgpool"
cd /tmp/pgpool-II-4.5.5 && \
    ./configure && \
    make && \
    make install
export PATH=/usr/local/pgpool/bin:$PATH
pwd
if [ $? -ne 0 ]; 
then
    echo "installing pgpool failed"
fi
echo "PGPOOL installed successfully"
