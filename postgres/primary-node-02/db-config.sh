echo "Configuring postgres"

chown -R postgres:postgres ${PGDATA}
chmod 700 ${PGDATA}

if [ ! -f "${PGDATA}/PG_VERSION" ]; then
  echo "PGDATA directory not initialized. Initializing cluster in ${PGDATA} ..."
  initdb -D ${PGDATA}
fi

if [ ! -f "/var/lib/postgresql/archive" ]; then
  echo "Archive directory not created, creating it now"
  mkdir -p /var/lib/postgresql/archive
  chown postgres:postgres /var/lib/postgresql/archive
fi

cat >> /etc/postgresql/pg_hba.conf << EOF
  host replication ${DB_REP_USER} 172.16.238.0/24 md5
  host all all 0.0.0.0/0 scram-sha-256
EOF

cat >> /etc/postgresql/postgresql.conf << EOF
  listen_addresses = '*'
  wal_level = logical
  archive_mode = on
  archive_command = 'cp %p /var/lib/postgresql/archive/%f'
  max_wal_senders = 10
  max_replication_slots = 5
  wal_keep_size = 512MB
  hot_standby = on
  synchronous_commit = local
  password_encryption = scram-sha-256
  pgpool.pg_ctl = '/usr/local/pgsql/bin/pg_ctl'
  shared_preload_libraries = 'repmgr'
EOF