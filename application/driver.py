
import utils
import setup


def execute(conn):
    conn.autocommit = False
    cursor = conn.cursor()
    partial_results = []
    final_result = []
    # Runnable queries
    queries = []

    # Tune the database
    setup.tune(conn)
    # Load the queries from the queries.sql file
    queries.extend(utils.load_queries(conn, 'ccb_queries.sql'))
    queries.extend(utils.load_queries(conn, 'cci_queries.sql'))
    # queries.extend(utils.load_queries(conn, 'cca_queries.sql'))

    # Execute each  low complexity query and store the result
    for i, query in enumerate(queries, start=1): 
        for _ in range(0, 9):
            execution_time = utils.run_query(cursor, query['action'])
            partial_results.append(execution_time)
        conn.commit()
        average = utils.calculate_average(partial_results)
        standard_deviation = utils.calculate_standard_deviation(partial_results, average)
        final_result.append({'description': query['description'], 'average': average, 'standard_deviation': standard_deviation, 'type': query['type']})
        print(f'Query {i} of {len(queries)} completed')
    
    utils.write_csv(final_result)
    setup.untune(conn)
    cursor.close()
    return final_result

