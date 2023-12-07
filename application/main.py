import os
import driver
import psycopg2
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), '../config/app-database.config.env')
)

# Get the database connection details from environment variables
db_host = os.environ.get('APP_DB_HOST')
pgpool_db_port = os.environ.get('APP_PGPOOL_DB_PORT')
clusterless_db_port = os.environ.get('APP_DB_CLUSTERLESS_PORT')
db_name = os.environ.get('APP_DB_NAME')
db_user = os.environ.get('APP_DB_USER')
db_password = os.environ.get('APP_DB_PASSWORD')


try: 
    # Connect to the clusterized databases using pgpool
    clusterized_conn = psycopg2.connect(
        host=db_host,
        port=pgpool_db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    # Connect to the clusterless databases 
    clusterless_conn = psycopg2.connect(
        host=db_host,
        port=clusterless_db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Execute the queries - clusterized databases
    driver.execute(clusterized_conn, 'clusterlized_query_times.csv')
    # Execute the queries - clusterized databases
    driver.execute(clusterless_conn, 'clusterless_query_times.csv')

    clusterized_conn.close()
    clusterless_conn.close()
except Exception as e:
    print(e)
    exit(1)