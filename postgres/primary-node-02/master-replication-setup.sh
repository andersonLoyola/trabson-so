#!/bin/bash
set -e

# Initialize the database cluster if PGDATA is not valid

echo "Creating physical replication slot 'replication_slot' if it doesn't exist..."
psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-'EOSQL'
  SELECT * FROM pg_create_physical_replication_slot('replication_slot')
  WHERE NOT EXISTS (
    SELECT 1 FROM pg_replication_slots WHERE slot_name = 'replication_slot'
  );
EOSQL


