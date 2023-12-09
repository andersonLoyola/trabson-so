import os
import csv
from time import time

def run_query(cursor, query):
    start = time() * 1000
    cursor.execute(query)
    cursor.fetchall()
    end = time() * 1000
    return end - start

def load_queries(query_type, filename =  'queries.sql'):
    queries = []
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as queries_file:
        query_type = filename.replace('_queries.sql', '')
        for line in queries_file:
            if line.startswith('--'):
                description = line.replace('--', '').strip()
                continue
            if line == '\n':
                continue
            queries.append({'description': description, 'action': line.strip(), 'type': query_type})
        return queries

def calculate_average(results):
    average = 0
    for result in results:
        average += result
    return average / len(results)


def calculate_standard_deviation(results, average):
    sum = 0
    for result in results:
        sum += (result - average) ** 2
    return (sum / len(results)) ** 0.5

def calculate_sample_variance(results, average):
    sum = 0
    for result in results:
        sum += (result - average) ** 2
    return sum / (len(results) - 1)


def write_csv(results, file_path = 'report'):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['description', 'average', 'standard_deviation', 'individual_results', 'min', 'max', 'type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
            print(f'{result["description"]}: {result["average"]} ms')
    print('Report generated successfully')

