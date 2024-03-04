from sqlalchemy import select, update, delete, insert, and_, all_, or_, any_, func, Table, alias
from psycopg2.extras import NamedTupleConnection, NamedTupleCursor
from enum import IntEnum
import datetime

class Status(IntEnum):
    TO_DO = 0
    IN_PROGRESS = 1
    DONE = 2


# with NamedTupleConnection(dsn="postgres://admin:admin@217.76.60.77:6666/admin") as connection:
#     with connection.cursor() as cursor:  # type: NamedTupleCursor
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS projects (
#                 id SERIAL PRIMARY KEY ,
#                 name VARCHAR ( 32 ) NOT NULL UNIQUE
#             );
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS task (
#                 id SERIAL PRIMARY KEY ,
#                 FOREIGN KEY (project_id) REFERENCES project(id),
#                 title VARCHAR(32) NOT NULL,
#                 description TEXT ,
#                 start_date TIMESTAMP NOT NULL,
#                 end_date TIMESTAMP NOT NULL,
#                 FOREIGN KEY (author_id) REFERENCES users(id),
#                 FOREIGN KEY (executor_id) REFERENCES users(e_id),
#                 status ENUM NOT NULL
#             );
#         """)
#         cursor.execute("""
#                     CREATE TABLE IF NOT EXISTS users (
#                         id SERIAL PRIMARY KEY ,
#                         e_id SERIAL PRIMARY KEY
#                     );
#                 """)
#         connection.commit()
#
# q = select(users).join()
# q = filter

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
    TIMESTAMP,
    ForeignKey,
    CheckConstraint,
    TEXT,
    create_engine, inspect
)
from sqlalchemy.orm import DeclarativeBase, declarative_base, relationship, sessionmaker

class Base(DeclarativeBase):
    ...

class project(Base):
    __tablename__ = 'projects'
    id = Column(int, primary_key=True)
    name = Column(VARCHAR(32), nullable=False)

class tasks(Base):
    __tablename__ = 'tasks'
    id = Column(int, primary_key=True)
    project_id = Column(int, ForeignKey(column="project.id"), nullable=True)
    title = Column(TEXT)
    start_date = Column(TIMESTAMP, nullable=True)
    author_id = Column(int, ForeignKey(column="users.id"), nullable=True)
    executor_id = Column(int, ForeignKey(column="users.e_id"), nullable=True)
    status = Column(Status, nullable=True)

class users(Base):
    id = Column(int, primary_key=True)
    e_id = Column(int, primary_key=True)

q = select(users).join(tasks)
q = q.filter(
    or_(
        status != 2
    )
    (
        datetime.date < end_date
    )
)
