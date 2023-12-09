
import utils

def execute(conn, report_file):
    
    cursor = conn.cursor()
    partial_results = []
    final_result = []
    # Runnable queries
    queries = []

    queries.extend(utils.load_queries(conn, 'ccb_queries.sql'))
    queries.extend(utils.load_queries(conn, 'cci_queries.sql'))
    # queries.extend(utils.load_queries(conn, 'cca_queries.sql'))

    for i, query in enumerate(queries, start=1): 
        for _ in range(0, 10):
            execution_time = utils.run_query(cursor, query['action'])
            partial_results.append(execution_time)
        average = utils.calculate_average(partial_results)
        standard_deviation = utils.calculate_standard_deviation(partial_results, average)
        final_result.append({
            'description': query['description'], 
            'average': average, 
            'standard_deviation': standard_deviation,
            'type': query['type'],
            'individual_results': partial_results,
            'min': min(partial_results),
            'max': max(partial_results),
        })
        print(f'Query {i} of {len(queries)} completed')
        partial_results = []
    
    utils.write_csv(final_result, report_file)
    cursor.close()
    return final_result

