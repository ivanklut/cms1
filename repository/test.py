def select_bu_id(table_name, ent_id):
    req = (
        f'SELECT content, title '
        f'FROM {table_name} '
        f'WHERE title > 1 '
        f'ORDER BY title ASC '
        f'LIMIT 2 OFFSET 1'
    )
    with sqlite3.connect(f'{CUR_DIR}\\{DB_NAME}.db') as conn:
        cur = conn.cursor()
        cur.execute(req)
        response = cur.fetchall()
        print(response)
    return response
