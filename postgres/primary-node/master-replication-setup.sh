#!/bin/bash
set -e

chown -R postgres:postgres ${PGDATA}
chmod 700 ${PGDATA}

# Initialize the database cluster if PGDATA is not valid
if [ ! -f "${PGDATA}/PG_VERSION" ]; then
  echo "PGDATA directory not initialized. Initializing cluster in ${PGDATA} ..."
  initdb -D ${PGDATA}
fi

cat >> ${PGDATA}/pg_hba.conf << EOF
  host replication all 0.0.0.0/0 md5
  host all all 0.0.0.0/0 scram-sha-256
EOF

cat >> ${PGDATA}/postgresql.conf << EOF
  listen_addresses = '*'
  wal_level = replica
  wal_keep_size = 64MB
  max_wal_senders = 10
  hot_standby = on
EOF

echo "Creating physical replication slot 'replication_slot' if it doesn't exist..."
psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-'EOSQL'
  SELECT * FROM pg_create_physical_replication_slot('replication_slot')
  WHERE NOT EXISTS (
    SELECT 1 FROM pg_replication_slots WHERE slot_name = 'replication_slot'
  );
EOSQL


exec "$@"