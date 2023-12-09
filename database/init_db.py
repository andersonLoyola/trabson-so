import psycopg2
import os
from dotenv import load_dotenv

def get_full_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def load_schema(conn, schema_file):
    cursor =  conn.cursor()
    with open(schema_file, 'r') as f:
        print('Creating schema...' + schema_file)
        cursor.execute(f.read())
        print(f'Schema {schema_file} created.')
    cursor.close()
    conn.commit()

def database_exists(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (os.getenv('APP_DB_NAME'),))
    exists = cursor.fetchone()
    cursor.close()
    return exists
        
def init_clustered_db(conn, schema_tables_name):
    if (database_exists(conn)):
        print('Database already exists - Skipping clustered db initialization.')
        return
    print('loading tables for clustered dbs ...')	
    for schema_file in schema_tables_name:
        load_schema(conn, get_full_path('tables/' + schema_file))
    print('loading data ...')	
    for schema_file in schema_tables_name:
        load_schema(conn, get_full_path('data/' + schema_file))


def init_clusterless_db(conn, schema_tables_name):
    if (database_exists(conn)):
        print('Database already exists - Skipping clusterless db initialization')
        return
    print('loading tables for clusterless dbs ...')	
    for schema_file in schema_tables_name:
        load_schema(clusterless_conn, get_full_path('tables/' + schema_file))
    print('loading data ...')	
    for schema_file in schema_tables_name:
        load_schema(clusterless_conn, get_full_path('data/' + schema_file))


if __name__ == '__main__':
    load_dotenv(dotenv_path=get_full_path('../config/app-database.config.env'))
    script_dir =  os.path.dirname(__file__)
    schema_tables_name = [
        'tb_domicilio.sql',
        'tb_esc.sql',
        'tb_mun.sql',
        'tb_pessoa.sql',
        'tb_trab.sql',
        'tb_fam.sql',
    ]

    db_host = os.getenv('APP_DB_HOST')
    db_user = os.getenv('APP_DB_USER')
    db_password = os.getenv('APP_DB_PASSWORD')
    db_name = os.getenv('APP_DB_NAME')
    pgpool_db_port = os.getenv('APP_PGPOOL_DB_PORT')
    clusterless_db_port = os.getenv('APP_DB_CLUSTERLESS_PORT')

    clusterized_conn = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        dbname=db_name,
        port=pgpool_db_port
    )
    
    clusterless_conn = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        dbname=db_name,
        port=clusterless_db_port
    )

    init_clustered_db(clusterized_conn, schema_tables_name)
    init_clusterless_db(clusterless_conn, schema_tables_name)

    clusterized_conn.close()
    clusterless_conn.close()