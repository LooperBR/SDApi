import sqlite3

def connect_db():
    conn = sqlite3.connect("dados")
    return conn

def create_table():
    conn = connect_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS compras(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            valor REAL NOT NULL,
            vencimento TEXT NOT NULL
        );
    ''')
    conn.close()

def get_id(id):
    item = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM compras 
            where id=?;
        ''',(id,))
        row = cursor.fetchone()
        item['id'] = row['id'],
        item['produto'] = row['produto'],
        item['valor'] = row['valor'],
        item['vencimento'] = row['vencimento']
    except sqlite3.Error as e:
        print(e)
        item = {}
    return item

def get_all():
    itens = {"compras":[]}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM compras;
        ''')
        rows = cursor.fetchall()
        for row in rows:
            item = {
                'id': row['id'],
                'produto': row['produto'],
                'valor': row['valor'],
                'vencimento': row['vencimento']
            }
            itens['compras'].append(item)
    except sqlite3.Error as e:
        print(e)
        print("erro get_all")
        itens = {"compras":[]}
    return itens

def insert(item):
    inserted_item = {}
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO compras(produto,valor,vencimento)
            VALUES (?,?,?);
        ''',
        (item['produto'],item['valor'],item['vencimento'])
        )
        conn.commit()
        print('comitado')
        inserted_item = get_id(cursor.lastrowid)
    except sqlite3.Error as e:
        print(e)
        print('rollback')
        conn.rollback()
    finally:
        print('close')
        conn.close()
    print('fim')
    return inserted_item

def update(item):
    update_item = {}
    try:
        conn = connect_db()
        cursor = conn.cursor()
        conn.rollback()
        cursor.execute('''
            UPDATE compras
            SET produto = ?, valor = ?, vencimento = ?
            where id = ?;
        ''',
        (item['produto'],item['valor'],item['vencimento'],item['id'])
        )
        conn.commit()
        update_item = get_id(item['id'])
    except:
        update_item = {}
    finally:
        conn.close()
    return update_item

def delete(id):
    message = {}
    try:
        produto = get_id(id)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM compras
            WHERE id = ?;
        ''',
        (id))
        conn.commit()
        if len(produto)>0:
            message['Estado'] = "Item deletado com sucesso"
        else:
            message['Estado'] = "Item não encontrado"
    except:
        conn.rollback()
        message['Estado'] = "Não foi possivel realzar a operação"
    finally:
        conn.close()
        
    return message
