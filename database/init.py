import psycopg2
import os
from dotenv import load_dotenv

def get_full_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def create_database(cursor):
    cursor.execute('CREATE DATABASE ' + os.getenv('DB_NAME'))

def load_schema(conn, schema_file):
    cursor =  conn.cursor()
    with open(schema_file, 'r') as f:
        print('Creating schema...' + schema_file)
        cursor.execute(f.read())
        print(f'Schema {schema_file} created.')
    cursor.close()
    conn.commit()
        


if __name__ == '__main__':
    script_dir =  os.path.dirname(__file__)
    schema_tables_name = [
        'tb_domicilio.sql',
        'tb_esc.sql',
        'tb_mun.sql',
        'tb_pessoa.sql',
        'tb_trab.sql',
    ]
    load_dotenv(dotenv_path=get_full_path('../config/app-database.config.env'))
    db_host = os.getenv('APP_DB_HOST')
    db_user = os.getenv('APP_DB_USER')
    db_password = os.getenv('APP_DB_PASSWORD')
    db_name = os.getenv('APP_DB_NAME')
    db_port = os.getenv('APP_DB_PORT')


    conn = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        dbname=db_name,
        port=db_port
    )
    print('loading tables ...')	
    for schema_file in schema_tables_name:
        load_schema(conn, get_full_path('tables/' + schema_file))
    print('loading data ...')	
    for schema_file in schema_tables_name:
        load_schema(conn, get_full_path('data/' + schema_file))
    conn.close()