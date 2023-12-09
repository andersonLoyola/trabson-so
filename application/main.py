import os
import use_cases
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

    clusterized_conn.autocommit = True
    clusterless_conn.autocommit = True

    # Execute the use cases
    use_cases.use_case_01.execute(clusterless_conn, clusterized_conn)
    use_cases.use_case_02.execute(clusterless_conn, clusterized_conn)
    use_cases.use_case_03.execute(clusterless_conn, clusterized_conn)
    use_cases.use_case_04.execute(clusterless_conn, clusterized_conn)
    use_cases.use_case_05.execute(clusterless_conn, clusterized_conn)
    use_cases.use_case_06.execute(clusterless_conn, clusterized_conn)
    use_cases.use_case_07.execute(clusterless_conn, clusterized_conn)
    use_cases.use_case_08.execute(clusterless_conn, clusterized_conn)
    

    clusterized_conn.close()
    clusterless_conn.close()
except Exception as e:
    print(e)
    exit(1)