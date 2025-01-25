# Use case 02 - 
import os
from helpers import driver
from helpers import setup

def execute(
    clusterized_conn_info,
    clusterless_conn_info,
    master_cluster_conn_info,
):
    print(
    """
    ------------------------------------
    | Executing use case 06           |
    ------------------------------------
    Tunning scenario 02: Max connection = 4, shared buffers = 2048mb 
    indexes for all used tables enabled
    """
    )
    # Get conections
    clusterized_conn = driver.get_connection(**clusterized_conn_info)
    clusterless_conn = driver.get_connection(**clusterless_conn_info)
    master_cluster_conn = driver.get_connection(**master_cluster_conn_info)
    # Set autocommit
    clusterized_conn.autocommit = True
    clusterless_conn.autocommit = True
    master_cluster_conn.autocommit = True
    # Create indexes
    setup.create_indexes_scenario(clusterless_conn)
    setup.create_indexes_scenario(master_cluster_conn)
    
    # Tunning scenario 02
    setup.create_tunning_scenario_02(clusterless_conn)
    setup.create_tunning_scenario_02(master_cluster_conn)
    
    
    report_dir_path = os.path.join(os.path.dirname(__file__), '../reports/use_case_06')
    os.makedirs(report_dir_path, exist_ok=True)
    driver.execute(clusterless_conn, f'{report_dir_path}/clusterless_query_times.csv')
    driver.execute(clusterized_conn, f'{report_dir_path}/clusterlized_query_times.csv')
    
    setup.drop_all_indexes(clusterless_conn)
    setup.drop_all_indexes(master_cluster_conn)
    

    setup.reset_tunning_scenarios(clusterless_conn)
    setup.reset_tunning_scenarios(master_cluster_conn)


    master_cluster_conn.close()
    
    clusterless_conn.close()
    clusterized_conn.close()
    