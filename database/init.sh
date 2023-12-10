#!/bin/bash
echo "Installing dependencies..."
pip install psycopg2
pip install python-dotenv
pip install pandas
echo "Dependencies installed!"
echo "loading environment host variables..."	
export APP_CLUSTERIZED_DB_HOST=pgpool
export APP_CLUSTERLESS_DB_HOST=clusterless-pg
export APP_DB_PORT=5432
echo "initializing database..."
python3 ./database/init_db.py
echo "Running performance script..."
python3 ./application/main.py