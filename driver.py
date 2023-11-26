from time import time
import reporter


def load_queries(filename =  'queries.sql'):
    queries= []
    with open(filename, 'r') as queries_file:
        for line in queries_file:
            if line.startswith('--'):
                description = line.replace('--', '').strip()
                continue
            if line == '\n':
                continue
            queries.append({'description': description, 'action': line.strip()})
        return queries


def run_query(cursor, query):
    start = time() * 1000
    cursor.execute(query)
    cursor.fetchall()
    end = time() * 1000
    return end - start
    
def execute(conn, queries, scenario = 'scenario_01'):
    conn.autocommit = False
    cursor = conn.cursor()
    results = []
    # Execute each  low complexity query and store the result
    for i, query in enumerate(queries['ccb'], start=1): 
        execution_time = run_query(cursor, query['action'])
        print(f"Tempo de execução da consulta ccb{i}: {execution_time:.4f} milisegundos\n")
        results.append({'query': f'ccb{i}', 'execution_time': execution_time, 'query_description':  query['description'], 'query_type': 'ccb'})
    # Execute each  medium complexity query and store the result
    for i, query in enumerate(queries['cci'], start=1): 
        execution_time = run_query(cursor, query['action'])
        print(f"Tempo de execução da consulta cci{i}: {execution_time:.4f} milisegundos\n")
        results.append({'query': f'cci{i}', 'execution_time': execution_time, 'query_description':  query['description'], 'query_type': 'cci'})
    # Execute each  higher complexity query and store the result
    for i, query in enumerate(queries['cca'], start=1): 
        execution_time = run_query(cursor, query['action'])
        print(f"Tempo de execução da consulta cca{i}: {execution_time:.4f} milisegundos\n")
        results.append({'query': f'cca{i}', 'execution_time': execution_time, 'query_description':  query['description'], 'query_type': 'cca'})
    reporter.execute(results, f'{scenario}')
    conn.commit()
    cursor.close()
    return results
