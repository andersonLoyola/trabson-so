import pandas as pd
import matplotlib.pyplot as plt
import csv

def write_csv(results, filename):
    with open(f'{filename}.csv', 'w', newline='') as csvfile:
        fieldnames = ['query', 'execution_time', 'query_type', 'query_description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def execute(results, filename): 
    df = pd.DataFrame(results)
    plt.figure(figsize=(200,100))
    df['execution_time'] = df['execution_time'].astype(float).round(6)
    df.plot(kind='bar', x='query', y='execution_time')
    plt.xlabel('query')
    plt.ylabel('Time (ms)')
    plt.title('Execution time for each query')
    plt.savefig(f'{filename}.png', format='png')
    write_csv(results, filename)