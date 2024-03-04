from psycopg2 import connect
from psycopg2._psycopg import cursor
from psycopg2.extras import NamedTupleCursor
from datetime import datetime

with connect(dsn="postgres://user10:thmCHbHR0.76.60.77:6666/user10", cursor_factory=NamedTupleCursor) as conn:
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                department_id INTEGER FOREIGN KEY,
                sub_department_id INT FOREIGN KEY
                
        );
    """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS departments(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(32)
        );
    """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sub_departments(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(32)
        );
    """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS chats(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(32)
        );
    """)
        cur.execute("""
             CREATE TABLE IF NOT EXISTS chats_relations(
                    id SERIAL PRIMARY KEY,
                    chat_id INTEGER PRIMARY KEY NOT NULL,
                    department_id INTEGER FOREIGN KEY,
                    sub_department_id INTEGER FOREIGN KEY
                    
        );
    """)
cur.commit()

cur.execute("""
            SELECT chats.name, chats.id
            FROM users INNER JOIN departments ON users.department_id = departments.id
            INNER JOIN sub_departments ON users.sub_department_id = sub_departments.id
            FROM chats_relations INNER JOIN departments ON chats_relations.department_id = departments.id
            INNER JOIN sub_departments ON chats_relations.sub_department_id = sub_departments.id
            INNER JOIN chats ON chats_relations.chat_id = chats.id
            WHERE  (user.department_id != null and chats_relations.department_id != null) or
            (user.department_id != null and chats_relations.department_id = null) or
            (user.sub_department_id != null and chats_relations.sub_department_id != null)
            (user.sub_department_id != null and chats_relations.sub_department_id = null) and 
             user.department_id = chats_relations.department_id or 
             user.sub_department_id = chats_relations.sub_department_id
             
""")
