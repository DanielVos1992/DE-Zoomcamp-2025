#!/bin/bash

set -e
set -u

echo "Running initialization script..."

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE ny_taxi;
    CREATE DATABASE kestra;
    
    \c ny_taxi
    CREATE SCHEMA IF NOT EXISTS public;
    GRANT ALL ON SCHEMA public TO postgres;
    
    \c kestra
    CREATE SCHEMA IF NOT EXISTS public;
    GRANT ALL ON SCHEMA public TO postgres;
EOSQL

echo "Database initialization completed!"