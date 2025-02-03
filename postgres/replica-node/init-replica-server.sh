#!/bin/bash
set -e
set_correct_folder_permission () {
   chmod 700 ${PGDATA}
}
wait_for_master () {
RETRY_COUNT=0
until pg_isready -h ${PRIMARY_DB_HOST} -p ${PRIMARY_DB_PORT}; do
    check_retry_count $RETRY_COUNT
    ((RETRY_COUNT=RETRY_COUNT+1))
    echo "$(date) - waiting for master postgres (${PRIMARY_DB_HOST}) to be ready..."
    sleep 3s
  done
}
check_retry_count () {
  RETRY_COUNT=$1
  MAX_RETRY=10
  if [ $RETRY_COUNT -eq $MAX_RETRY ]; then
    echo "Maximum retry for checking master DB to be online is reached, exiting..."
    exit 3
  fi
}
take_basebackup () {
  echo "Removing contents from PGDATA dir.. "
  rm -rf ${PGDATA}/*
  echo "Contents of PGDATA folder: "
  ls -l ${PGDATA}
  echo "Taking basebackup of the primary DB .."
  export PGPASSWORD=${PRIMARY_DB_REP_USER_PASS}
  pg_basebackup -h ${PRIMARY_DB_HOST} -p ${PRIMARY_DB_PORT} -U ${PRIMARY_DB_REP_USER} -D ${PGDATA} -c fast -X stream -R -w -P
  unset PGPASSWORD
  
  echo "Done taking backup of the primary DB.."
  echo "NEW Contents of PGDATA folder: "
  ls -l ${PGDATA}
}
write_trigger_file_to () {
  file_path=$1
  echo "trigger_file = '/tmp/promote_me_to_master' " >> $file_path
}

add_standby_configuration () {
  # Create standby.signal file to enable standby mode
  touch ${PGDATA}/standby.signal
  # Append replication settings to postgresql.conf
  cat >> "${PGDATA}/postgresql.conf" <<EOF
primary_conninfo = 'host=${PRIMARY_DB_HOST} port=${PRIMARY_DB_PORT} user=${DB_REP_USER} password=${DB_REP_PASS}'
primary_slot_name = 'replication_slot'
EOF
}

# If standby is not yet configured, perform the base backup and add standby configuration.
if [ ! -f "${PGDATA}/standby.signal" ]; then
  set_correct_folder_permission
  wait_for_master
  take_basebackup
  add_standby_configuration
fi
exec "$@"