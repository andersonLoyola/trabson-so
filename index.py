import os
import psycopg2
import driver
import setup
from dotenv import load_dotenv

load_dotenv() 
results = []
queries = {
    "ccb": [],
    "cci": [],
    "cca": []
}

# Get the database connection details from environment variables
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# Connect to the database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)


# Read the queries from the queries.sql file
queries['ccb'] = driver.load_queries('ccb_queries.sql')
queries['cci'] = driver.load_queries('cci_queries.sql')
queries['cca'] = driver.load_queries('cca_queries.sql')

# Execute the queries and store the results
try:
    # Scenario 1: Default configuration without any tuning without indexes
    setup.drop_all_indexes(conn)
    setup.reset_tunning_scenarios(conn)
    print('Executing scenario 1...')
    driver.execute(conn, queries)
    # Scenario 2: Default configuration without any tuning with indexes
    print('Executing scenario 2...')
    setup.create_indexes_scenario(conn)
    driver.execute(conn, queries, 'scenario_02')
    setup.drop_all_indexes(conn)
    # Scenario 3: Tunning scenario 1 - Max connections = 4 without indexes
    print('Executing scenario 3...')
    setup.create_tunning_scenario_01(conn)
    driver.execute(conn, queries, 'scenario_03')
    print('Resetting database configuration...')
    setup.reset_tunning_scenarios(conn)
    # Scenario 4: Tunning scenario 1 - Max connections = 4 with indexes
    print('Executing scenario 4...')
    setup.create_tunning_scenario_01(conn)
    setup.create_indexes_scenario(conn)
    driver.execute(conn, queries, 'scenario_04')
    print('Resetting database configuration...')
    setup.reset_tunning_scenarios(conn)
    setup.drop_all_indexes(conn)
    # Scenario 5: Tunning scenario 2 - Max connections = 4, shared buffers = 2048mb without indexes
    print('Executing scenario 5...')
    setup.create_tunning_scenario_02(conn)
    driver.execute(conn, queries, 'scenario_05')
    print('Resetting database configuration...')
    setup.reset_tunning_scenarios(conn)
    # Scenario 6: Tunning scenario 2 - Max connections = 4, shared buffers = 2048mb with indexes
    print('Executing scenario 6...')
    setup.create_tunning_scenario_02(conn)
    setup.create_indexes_scenario(conn)
    driver.execute(conn, queries, 'scenario_06')
    print('Resetting database configuration...')
    setup.reset_tunning_scenarios(conn)
    setup.drop_all_indexes(conn)
    # Scenario 7: Tunning scenario 3 - Max connections = 4, shared buffers = 2048mb, effective_cache_size= 6gb without indexes
    print('Executing scenario 7...')
    setup.create_tunning_scenario_03(conn)
    driver.execute(conn, queries, 'scenario_07')
    print('Resetting database configuration...')
    setup.reset_tunning_scenarios(conn)
    # Scenario 8: Tunning scenario 3 - Max connections = 4, shared buffers = 2048mb, effective_cache_size= 6gb with indexes
    print('Executing scenario 8...')
    setup.create_tunning_scenario_03(conn)
    setup.create_indexes_scenario(conn)
    driver.execute(conn, queries, 'scenario_08')
    print('Resetting database configuration...')
    setup.reset_tunning_scenarios(conn)
    setup.drop_all_indexes(conn)
   
    # Close the connection
    conn.close()
except Exception as e:
    print(f'Error: {e}')





