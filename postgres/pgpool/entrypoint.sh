#!/bin/bash
export PATH="/usr/local/bin:$PATH"

./usr/local/bin/pgpool-setup.sh

if [ $? -ne 0 ]; 
then
    echo "pgpool-setup.sh failed"
    exit 1
fi

./usr/local/bin/replication-setup.sh

if [ $? -ne 0 ]; 
then
    echo "replication-setup.sh failed"
    exit 1
fi

./usr/local/bin/init_app_db.sh

if [ $? -ne 0 ]; 
then
    echo "init_app_db.sh failed"
    exit 1
fi

ls /usr/local/etc/pgpool
echo "Both scripts executed successfully"
exec "$@"

