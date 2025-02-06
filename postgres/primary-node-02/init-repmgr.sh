echo "Create master-master replication (logical)"
cat >> /var/lib/postgresql/repmgr.conf << EOF
  node_id=2
  node_name='primary-node-02'
  conninfo='host=${PRIMARY_NODE_HOST_02} user=${DB_REP_USER} dbname=repmgr connect_timeout=2'
  data_directory='/var/lib/postgresql/17/main'
  use_replication_slots=yes
EOF

echo "Executing rpmgr"
repmgr -f /var/lib/postgresql/repmgr.conf standby register --force