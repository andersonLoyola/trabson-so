# Use case 02 - 
import os
import setup
import driver


def execute(conn, clusterized_conn):
    print(
        """
        ------------------------------------
        | Executing use case 04            |
        ------------------------------------
        Tunning scenario 01: Max connection = 4 
        indexes for all used tables enabled
        """
    )
    setup.create_indexes_scenario(conn)
    setup.create_tunning_scenario_01(conn)
    report_dir_path = os.path.join(os.path.dirname(__file__), '../reports/use_case_04')
    os.makedirs(report_dir_path, exist_ok=True)
    driver.execute(conn, f'{report_dir_path}/clusterless_query_times.csv')
    driver.execute(clusterized_conn, f'{report_dir_path}/clusterlized_query_times.csv')
    setup.drop_all_indexes(conn)
    setup.reset_tunning_scenarios(conn)
    