from sqlalchemy import select, update, delete, insert, and_, all_, or_, any_, func, Table, alias, INT
from psycopg2.extras import NamedTupleConnection, NamedTupleCursor
from enum import IntEnum
import datetime

class Status(IntEnum):
    TO_DO = 0
    IN_PROGRESS = 1
    DONE = 2


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
    id = Column(INT, primary_key=False)
    name = Column(VARCHAR(32), nullable=False)

class tasks(Base):
    __tablename__ = 'tasks'
    id = Column(INT, primary_key=True)
    project_id = Column(INT, ForeignKey(column="project.id"), nullable=False)
    title = Column(TEXT)
    start_date = Column(TIMESTAMP, nullable=False)
    author_id = Column(INT, ForeignKey(column="users.id"), nullable=False)
    executor_id = Column(INT, ForeignKey(column="users.e_id"), nullable=False)
    status = Column(Status, nullable=False)

class users(Base):
    id = Column(INT, primary_key=False)
    e_id = Column(INT, primary_key=False)

q = select(users).join(tasks)
q = q.filter(
    or_(
        tasks.status != 2
    )
    (
        datetime.date < tasks.end_date
    )
)


