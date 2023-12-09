# Use case 02 - 
import os
from helpers import driver
from helpers import setup


def execute(conn, clusterized_conn):
    print(
        """
        ------------------------------------
        | Executing use case 02            |
        ------------------------------------
        Tunning scenario 00: No tunning
        indexes for all used tables enabled
        """
    )
    setup.create_indexes_scenario(conn)
    report_dir_path = os.path.join(os.path.dirname(__file__), '../reports/use_case_02')
    os.makedirs(report_dir_path, exist_ok=True)
    driver.execute(conn, f'{report_dir_path}/clusterless_query_times.csv')
    driver.execute(clusterized_conn, f'{report_dir_path}/clusterlized_query_times.csv')
    setup.drop_all_indexes(conn)
    setup.drop_all_indexes(clusterized_conn)
    