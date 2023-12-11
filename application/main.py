import os
import use_cases
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), '../config/app-database.config.env')
)

# Get the database connection details from environment variables
clusterized_db_host = os.environ.get('APP_CLUSTERIZED_DB_HOST') or 'localhost'
clusterless_db_host = os.environ.get('APP_CLUSTERLESS_DB_HOST') or 'localhost'	
master_cluster_db_host = os.environ.get('APP_CLUSTER_01_DB_HOST') or 'localhost'		
pgpool_db_port = os.getenv('APP_DB_PORT') or 5432 # default pgpool port configured on docker-compose.yml
clusterless_db_port = os.getenv('APP_DB_PORT') or 5436  # default clusterless-pg port configured on docker-compose.yml
master_cluster_port = os.getenv('APP_DB_PORT') or 5430  # default cluster-01 which is the master node configured on docker-compose.yml
db_name = os.environ.get('APP_DB_NAME')
db_user = os.environ.get('APP_DB_USER')
db_password = os.environ.get('APP_DB_PASSWORD')


try: 
    # Connect to the clusterized databases using pgpool
    clusterless_conn_info = {
        'host': clusterless_db_host,
        'port': clusterless_db_port,
        'dbname': db_name,
        'user': db_user,
        'password': db_password
    }

    master_cluster_conn_info = {
        'host': master_cluster_db_host,
        'port': master_cluster_port,
        'dbname': db_name,
        'user': db_user,
        'password': db_password
    }

    clusterized_conn_info = {
        'host': clusterized_db_host,
        'port': pgpool_db_port,
        'dbname': db_name,
        'user': db_user,
        'password': db_password
    }

    # Execute the use cases
    use_cases.use_case_01.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
    )
    use_cases.use_case_02.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
        master_cluster_conn_info=master_cluster_conn_info,
    )
    use_cases.use_case_03.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
        master_cluster_conn_info=master_cluster_conn_info,
    )
    use_cases.use_case_04.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
        master_cluster_conn_info=master_cluster_conn_info,
    )
    use_cases.use_case_05.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
        master_cluster_conn_info=master_cluster_conn_info,
     
    )
    use_cases.use_case_06.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
        master_cluster_conn_info=master_cluster_conn_info,
    )
    use_cases.use_case_07.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
        master_cluster_conn_info=master_cluster_conn_info,
    )
    use_cases.use_case_08.execute(
        clusterized_conn_info=clusterized_conn_info,
        clusterless_conn_info=clusterless_conn_info,
        master_cluster_conn_info=master_cluster_conn_info,
    )
    

except Exception as e:
    print(e)
    exit(1)