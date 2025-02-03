#!/bin/bash

# Execute pgpool-setup.sh
./usr/local/bin/pgpool-setup.sh

# Check if pgpool-setup.sh executed successfully
if [ $? -ne 0 ]; 
then
    echo "pgpool-setup.sh failed"
    exit 1
fi

# Execute replication-setup.sh
./usr/local/bin/replication-setup.sh


if [ $? -ne 0 ]; 
then
    echo "replication-setup.sh failed"
    exit 1
fi
export PATH="/usr/local/bin:$PATH"
echo "Both scripts executed successfully"
exec "$@"