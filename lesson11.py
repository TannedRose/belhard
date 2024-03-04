from psycopg2.extras import NamedTupleConnection, NamedTupleCursor

with NamedTupleConnection(dsn="postgres://admin:admin@217.76.60.77:6666/admin") as connection:
    with connection.cursor() as cursor:  # type: NamedTupleCursor
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id SERIAL PRIMARY KEY ,
                name VARCHAR ( 32 ) NOT NULL UNIQUE
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sub_departments (
                id SERIAL PRIMARY KEY ,
                name VARCHAR ( 32 ) NOT NULL UNIQUE
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY ,
                department_id INTEGER ,
                sub_department_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES departments(id),
                FOREIGN KEY (sub_department_id) REFERENCES sub_departments(id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id SERIAL PRIMARY KEY ,
                name VARCHAR ( 32 ) NOT NULL UNIQUE
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_relations (
                id SERIAL PRIMARY KEY ,
                chat_id INTEGER NOT NULL ,
                department_id INTEGER ,
                sub_department_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES departments(id),
                FOREIGN KEY (sub_department_id) REFERENCES sub_departments(id),
                FOREIGN KEY (chat_id) REFERENCES chats(id)
            );
        """)
        connection.commit()
        cursor.execute(query="""
            SELECT chats.name FROM chat_relations
            JOIN chats ON chats.id  = chat_relations.chat_id
            WHERE (
                chat_relations.department_id IS NULL OR
                chat_relations.department_id = (
                    SELECT users.department_id FROM users WHERE users.id = %(user_id)s
                )
            ) AND (
                chat_relations.sub_department_id IS NULL OR
                chat_relations.sub_department_id = (
                    SELECT users.sub_department_id FROM users WHERE users.id = %(user_id)s
                )
            );
        """, vars={"user_id": 3})
        print(cursor.fetchall())
