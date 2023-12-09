#!/bin/bash
echo "Installing dependencies..."
pip install psycopg2
pip install python-dotenv
pip install pandas
echo "Dependencies installed!"
echo "initializing database..."
python3 ./database/init_db.py