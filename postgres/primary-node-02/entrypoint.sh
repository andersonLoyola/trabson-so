#!/bin/bash
set -e

./usr/local/bin/db-config.sh
./usr/local/bin/master-replication-setup.sh

echo "initializing postgres"
pg_ctl -D /var/lib/postgresql/data -l logfile start
echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h localhost -p 5432 -U "$POSTGRES_USER"; do
  sleep 1
done

./usr/local/bin/init-db.sh
./usr/local/bin/rpmgr-replication-setup.sh
