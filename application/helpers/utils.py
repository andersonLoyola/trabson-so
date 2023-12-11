import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
from time import time

def run_query(cursor, query):
    start = time() * 1000
    cursor.execute(query)
    cursor.fetchall()
    end = time() * 1000
    return end - start

def load_queries(query_type, filename =  'queries.sql'):
    queries = []
    with open(os.path.join(os.path.dirname(__file__), f'../queries/{filename}'), 'r') as queries_file:
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
        fieldnames = ['description', 'average', 'standard_deviation', 'individual_results', 'min', 'max', 'type', 'id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print('Report generated successfully')

def plot_graph(results, filename): 
    df = pd.DataFrame(results)
    plt.figure(figsize=(200,100))
    # Convert 'average' and 'standard_deviation' to float and round to 6 decimal places
    df['execution_time'] = df['average'].astype(float).round(6)
    df['std_dev'] = df['standard_deviation'].astype(float).round(6)
    # Create a bar plot for the average execution time
    df.plot(
        kind='barh',
        x='id', 
        y='execution_time', 
        color='blue',
        label='Mean',
        capsize=5, 
        rot=0
    )
    # Overlay a bar plot for the standard deviation
    df.plot(
        kind='barh',
        x='id', 
        y='std_dev', 
        color='red',
        label='Standard Deviation',
        capsize=5, 
        rot=0,
        ax=plt.gca()  # Use the same axes for the second plot
    )
    plt.xlabel('Time (ms)')
    plt.ylabel('query id')
    plt.title('Average Execution time and Standard Deviation for each query')
    plt.legend()
    plt.savefig(filename, format='png')
    plt.close()