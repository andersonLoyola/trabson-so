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

def table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s)", 
        (table_name,)
    )
    exists = cursor.fetchone()[0]
    cursor.close()
    return exists
        
def init_clustered_db(conn, schema_tables_name):
    print('loading tables for clustered dbs ...')	
    for schema_file in schema_tables_name:
        table_name = schema_file.split('.')[0]
        if (table_exists(conn, table_name)):
            print(f'Table {table_name} already exists - Skipping clustered db initialization.')
            continue
        load_schema(conn, get_full_path('tables/' + schema_file))
    print('loading data ...')	
    for schema_file in schema_tables_name:
        load_schema(conn, get_full_path('data/' + schema_file))


def init_clusterless_db(conn, schema_tables_name):
    print('loading tables for clusterless dbs ...')	
    for schema_file in schema_tables_name:
        table_name = schema_file.split('.')[0]
        if (table_exists(conn, table_name)):
            print(f'Table {table_name} already exists - Skipping clustered db initialization.')
            continue
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
        'tb_familia.sql',
    ]

    clusterized_db_host = os.environ.get('APP_CLUSTERIZED_DB_HOST') or 'localhost'
    clusterless_db_host = os.environ.get('APP_CLUSTERLESS_DB_HOST') or 'localhost'	
    db_user = os.getenv('APP_DB_USER')
    db_password = os.getenv('APP_DB_PASSWORD')
    db_name = os.getenv('APP_DB_NAME')
    pgpool_db_port = os.getenv('APP_DB_PORT') or 5432 # default pgpool port configured on docker-compose.yml
    clusterless_db_port = os.getenv('APP_DB_PORT') or 5436  # default clusterless-pg port configured on docker-compose.yml

    clusterized_conn = psycopg2.connect(
        host=clusterized_db_host,
        user=db_user,
        password=db_password,
        dbname=db_name,
        port=pgpool_db_port
    )
    
    clusterless_conn = psycopg2.connect(
        host=clusterless_db_host,
        user=db_user,
        password=db_password,
        dbname=db_name,
        port=clusterless_db_port
    )

    init_clustered_db(clusterized_conn, schema_tables_name)
    init_clusterless_db(clusterless_conn, schema_tables_name)

    clusterized_conn.close()
    clusterless_conn.close()