def tune(conn):
    conn.autocommit = True
    cursor = conn.cursor()
    tunning_stmts = [
        "ALTER SYSTEM SET shared_buffers = '2048MB';",
		"ALTER SYSTEM SET effective_cache_size = '6GB';",
    ]
    print('Tunning database...')
    for stmt in tunning_stmts:
        print(f'Executing: {stmt}')
        cursor.execute(stmt)
    conn.commit()
    print('Tunning completed')


def untune(conn):
    conn.autocommit = True
    cursor = conn.cursor()
    tunning_stmts = [
        "ALTER SYSTEM RESET shared_buffers;",
        "ALTER SYSTEM RESET effective_cache_size;",
    ]
    print('Untunning database...')
    for stmt in tunning_stmts:
        print(f'Executing: {stmt}')
        cursor.execute(stmt)
    conn.commit()
    print('Untunning completed')