def tune(conn):
    cursor = conn.cursor()
    tunning_stmts = [
        "ALTER SYSTEM SET shared_buffers = '2048MB';",
		"ALTER SYSTEM SET effective_cache_size = '6GB';",
    ]
    print('Tunning database...')
    for stmt in tunning_stmts:
        print(f'Executing: {stmt}')
        cursor.execute(stmt)
    print('Tunning completed')


def untune(conn):
    cursor = conn.cursor()
    tunning_stmts = [
        "ALTER SYSTEM RESET shared_buffers;",
        "ALTER SYSTEM RESET effective_cache_size;",
    ]
    print('Untunning database...')
    for stmt in tunning_stmts:
        print(f'Executing: {stmt}')
        cursor.execute(stmt)
    
    print('Untunning completed')

# indexes scenarios
def create_indexes_scenario(conn):
    cursor = conn.cursor()
    database_indexes_stmts = [
        "CREATE INDEX idx_docmicilio_comodos ON tb_domicilio(qtd_comodos_domic_fam);",
        "CREATE INDEX idx_pessoa_sexo ON tb_pessoa (cod_sexo_pessoa);",
        "CREATE INDEX idx_familia_ibge ON tb_familia (cd_ibge);",
        "CREATE INDEX idx_domicilio_material_piso ON tb_domicilio (cod_material_piso_fam);",
        "CREATE INDEX idx_pessoa_raca_cor ON tb_pessoa (cod_raca_cor_pessoa);",
        "CREATE INDEX idx_pessoa_familia ON tb_pessoa (id_familia, idade, cod_sexo_pessoa);",
        "CREATE INDEX idx_mun_ibge ON tb_mun (cd_ibge, uf);",
        "CREATE INDEX idx_trab_pessoa ON tb_trab (id_pessoa, cod_trabalho_12_meses_memb, cod_principal_trab_memb, val_remuner_emprego_memb);",
        "CREATE INDEX idx_domicilio_familia ON tb_domicilio (id_familia, qtd_comodos_domic_fam, COD_AGUA_CANALIZADA_FAM);",
        "CREATE INDEX idx_esc_pessoa ON tb_esc (id_pessoa, cod_curso_frequentou_pessoa_memb, cod_concluiu_frequentou_memb);",
        "CREATE INDEX idx_mun_ibge_regiao ON tb_mun (cd_ibge, regiao);",
        "CREATE INDEX idx_trab_pessoa_fam ON tb_trab (id_familia, id_pessoa, val_remuner_emprego_memb, cod_principal_trab_memb);",
        "CREATE INDEX idx_domicilio_familia_abast_agua ON tb_domicilio (id_familia, cod_abaste_agua_domic_fam, cod_local_domic_fam, cod_destino_lixo_domic_fam);",
        "CREATE INDEX idx_esc_freq_escola ON tb_esc (id_pessoa, ind_frequenta_escola_memb);"
    ]
    for stmt in database_indexes_stmts:
        cursor.execute(stmt)
    cursor.close()

def drop_all_indexes(conn):
    cur = conn.cursor()
    drop_indexes_stmts = [
        "DROP INDEX IF EXISTS idx_docmicilio_comodos;",
        "DROP INDEX IF EXISTS idx_domicilio_comodos;",
        "DROP INDEX IF EXISTS idx_pessoa_sexo;",
        "DROP INDEX IF EXISTS idx_familia_ibge;",
        "DROP INDEX IF EXISTS idx_domicilio_material_piso;",
        "DROP INDEX IF EXISTS idx_pessoa_raca_cor;",
        "DROP INDEX IF EXISTS idx_pessoa_familia;",
        "DROP INDEX IF EXISTS idx_mun_ibge;",
        "DROP INDEX IF EXISTS idx_trab_pessoa;",
        "DROP INDEX IF EXISTS idx_domicilio_familia;",
        "DROP INDEX IF EXISTS idx_esc_pessoa;",
        "DROP INDEX IF EXISTS idx_mun_ibge_regiao;",
        "drop index if exists idx_trab_pessoa_fam;",
        "drop index if exists idx_domicilio_familia_abast_agua;",
        "drop index if exists idx_esc_freq_escola;"
    ]
    # Execute the DROP INDEX commands
    for stmt in drop_indexes_stmts:
        cur.execute(stmt)

    # Commit the changes and close the connection
    cur.close()

def create_tunning_scenario_01(conn): 
    
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM SET max_connections = 4",
    ]
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    cursor.close()

def create_tunning_scenario_02(conn): 
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM SET max_connections = 4;",
        "ALTER SYSTEM SET shared_buffers = '2048MB';",
    ]
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    cursor.close()

def create_tunning_scenario_03(conn): 
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM SET max_connections = 4;",
        "ALTER SYSTEM SET shared_buffers = '2048MB';",
		"ALTER SYSTEM SET effective_cache_size = '6GB';",
    ]
    for stmt in database_config_stmts:    
        cursor.execute(stmt)
    cursor.close()

def reset_tunning_scenarios(conn):
    cursor = conn.cursor()
    database_config_stmts = [
        "ALTER SYSTEM RESET shared_buffers;",
        "ALTER SYSTEM RESET work_mem;",
        "ALTER SYSTEM RESET effective_cache_size;",
    ]
    for stmt in database_config_stmts:
        cursor.execute(stmt)
    cursor.close()
