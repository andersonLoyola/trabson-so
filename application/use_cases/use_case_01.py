# Use case 01 - no tunning and no indexess
import os
from helpers import driver
from helpers import setup


def execute(
    clusterized_conn_info,
    clusterless_conn_info,
):
    print(
    """
        ------------------------------------
    | Executing use case 01             |
    ------------------------------------
    Tunning scenario 00: No tunning 
    no indexes   
    """
    )
    clusterized_conn = driver.get_connection(**clusterized_conn_info)
    clusterless_conn = driver.get_connection(**clusterless_conn_info)
    # Set autocommit
    clusterized_conn.autocommit = True
    clusterless_conn.autocommit = True

    report_dir_path = os.path.join(os.path.dirname(__file__), '../reports/use_case_01')
    os.makedirs(report_dir_path, exist_ok=True)
    driver.execute(clusterized_conn, f'{report_dir_path}/clusterlized_query_times.csv')
    driver.execute(clusterless_conn, f'{report_dir_path}/clusterless_query_times.csv')
    clusterless_conn.close()
    clusterized_conn.close()
    