def create_tunning_scenario_01(conn): 
    conn.autocommit = True
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM SET max_connections = 4",
    ]
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    cursor.close()
    
def create_tunning_scenario_02(conn): 
    conn.autocommit = True
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM SET max_connections = 4;",
        "ALTER SYSTEM SET shared_buffers = '2048MB';",
    ]
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    cursor.close()

def create_tunning_scenario_03(conn): 
    conn.autocommit = True
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM SET max_connections = 4;",
        "ALTER SYSTEM SET shared_buffers = '2048MB';",
		"ALTER SYSTEM SET effective_cache_size = '6GB';",
    ]
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    cursor.close()

    
def reset_tunning_scenarios(conn):
    conn.autocommit = True
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM RESET shared_buffers;",
        "ALTER SYSTEM RESET work_mem;",
        "ALTER SYSTEM RESET effective_cache_size;",
    ]
    for stmt in database_config_stmts:
        cursor.execute(stmt)
    cursor.close()