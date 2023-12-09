# Use case 01 - no tunning and no indexess
import os
import driver
import setup


def execute(conn, clusterized_conn):
    print(
        """
         ------------------------------------
        | Executing use case 01             |
        ------------------------------------
        Tunning scenario 00: No tunning 
        no indexes   
        """
    )
    report_dir_path = os.path.join(os.path.dirname(__file__), '../reports/use_case_01')
    os.makedirs(report_dir_path, exist_ok=True)
    driver.execute(conn, f'{report_dir_path}/clusterless_query_times.csv')
    driver.execute(clusterized_conn, f'{report_dir_path}/clusterlized_query_times.csv')
    setup.drop_all_indexes(conn)
    setup.drop_all_indexes(clusterized_conn)
    