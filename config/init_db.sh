#!/bin/bash

# Variables
DB_NAME="mata58-so"
DB_USER="david"
DB_PASSWORD="donedummydonedummy"

# Create database
psql -U postgres -c "CREATE DATABASE $DB_NAME;"

# Create user and grant privileges
psql -U postgres -c "CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASSWORD';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"