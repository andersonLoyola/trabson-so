# Use case 02 - 
import os
import setup
import driver


def execute(conn, clusterized_conn):
    print(
        """
        ------------------------------------
        | Executing use case 08            |
        ------------------------------------
        Tunning scenario 03: Max connection = 4, shared buffers = 2048mb, effective_cache_size = 6gb  
        indexes for all used tables enabled
        """
    )
    setup.create_indexes_scenario(conn)
    setup.create_tunning_scenario_03(conn)
    report_dir_path = os.path.join(os.path.dirname(__file__), '../reports/use_case_08')
    os.makedirs(report_dir_path, exist_ok=True)
    driver.execute(conn, f'{report_dir_path}/clusterless_query_times.csv')
    driver.execute(clusterized_conn, f'{report_dir_path}/clusterlized_query_times.csv')
    setup.drop_all_indexes(conn)
    setup.drop_all_indexes(clusterized_conn)
    setup.reset_tunning_scenarios(conn)
    setup.reset_tunning_scenarios(clusterized_conn)
    