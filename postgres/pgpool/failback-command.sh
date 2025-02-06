#!/bin/bash
set -e

failed_node_id=$1
new_primary_node_id=$2
failed_host=$3
new_primary_host=$4

echo "Failback triggered. Failed node ID: $failed_node_id, New primary node ID: $new_primary_node_id, Failed host: $failed_host, New primary host: $new_primary_host"

# Reinitialize the failed node as a replica
if [ "$failed_node_id" -eq 0 ]; then
  ssh postgres@$failed_host "pg_basebackup -h $new_primary_host -D /var/lib/postgresql/data -U postgres -v -P --wal-method=stream"
  ssh postgres@$failed_host "touch /var/lib/postgresql/data/standby.signal"
  ssh postgres@$failed_host "pg_ctl start -D /var/lib/postgresql/data"
fi