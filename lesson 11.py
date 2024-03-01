# from psycopg2 import connect
# from psycopg2._psycopg import cursor
# from psycopg2.extras import NamedTupleCursor
from datetime import datetime

# postgres://username:password@host:port/db_name
# with connect(dsn="postgres://admin:admin@217.76.60.77:6666/admin", cursor_factory=NamedTupleCursor) as conn:
#     with conn.cursor() as cur:  # type: cursor
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS tags(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(16) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
        #     );
        # """)
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS topics(
        #         id SERIAL PRIMARY KEY,
        #         title VARCHAR(128) NOT NULL CHECK ( length(title) >= 2 ),
        #         body TEXT NOT NULL,
        #         date_created TIMESTAMP NOT NULL DEFAULT (now()),
        #         is_published BOOLEAN NOT NULL DEFAULT (false)
        #     );
        # """)
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS topic_tags(
        #         tag_id INTEGER,
        #         topic_id INTEGER,
        #         PRIMARY KEY (tag_id, topic_id),
        #         FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE RESTRICT ON UPDATE CASCADE,
        #         FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE RESTRICT ON UPDATE CASCADE
        #     );
        # """)
        # conn.commit()

        # cur.execute("drop table topic_tags;")
        # cur.execute("drop table topics;")
        # cur.execute("drop table tags;")
        # conn.commit()
        # tag_name = "POLITIC'); DROP TABLE test; insert into topics (title, body) values ('aa', 'aa"
        # cur.execute("""
        #     INSERT INTO tags (name) VALUES (%s);
        # """, ("MOTO", ))
        # conn.commit()
        # cur.execute("""
        #     SELECT * FROM tags WHERE lower(tags.name) like %s;
        # """, ("%o%", ))
        # print(cur.fetchall())
        # cur.execute("""
        #     SELECT lower(CONCAT(tags.name, ': ', topics.title, ': ', topics.id + 5)) as title
        #     FROM tags INNER JOIN topic_tags ON tags.id = topic_tags.tag_id
        #     INNER JOIN topics ON topic_tags.topic_id = topics.id
        #     WHERE topics.is_published = true;
        # """)
        # print(cur.fetchall())
        # cur.execute("""
        #     UPDATE topics SET is_published = true;
        # """)
        # conn.commit()
        # cur.execute("""
        #     SELECT tags.id, tags.name FROM tags WHERE
        #     tags.id IN (
        #         SELECT topics.id FROM topics WHERE topics.is_published = true
        #     );
        # """)
        # print(cur.fetchall())
        # cur.execute("""
        #     SELECT * FROM topics ORDER BY topics.is_published DESC, topics.date_created DESC;
        # """)
        # print(cur.fetchall())
        # cur.execute("""
        #     SELECT COUNT(topics) FROM topics WHERE topics.is_published = true;
        # """)
        # print(cur.fetchone())

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
    TIMESTAMP,
    ForeignKey,
    CheckConstraint,
    TEXT,
    create_engine
)
from sqlalchemy.orm import DeclarativeBase, declarative_base, relationship, sessionmaker

# SQLAlchemy < 2
# Base = declarative_base()


# SQLAlchemy >= 2
class Base(DeclarativeBase):
    ...


class Tag(Base):
    __tablename__ = "tags"
    __table_args__ = (
        CheckConstraint("length(name) >= 2"),
    )

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=16), nullable=False, unique=True)

    topics = relationship(argument="Topic", back_populates="tag")


class Topic(Base):
    __tablename__ = "topics"
    __table_args__ = (
        CheckConstraint("length(title) >= 2"),
        CheckConstraint("length(body) >= 2"),
    )

    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(length=128), nullable=False)
    body = Column(TEXT, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False, default=datetime.now, server_default="now()")
    is_published = Column(BOOLEAN, nullable=False, default=False, server_default="false")
    tag_id = Column(
        INT,
        ForeignKey(column=Tag.id, ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False
    )

    tag = relationship(argument=Tag, back_populates="topics")


engine = create_engine(url="postgresql://admin:admin@217.76.60.77:6666/admin")
session_maker = sessionmaker(bind=engine)


with session_maker() as session:
    tag = session.get(entity=Tag, ident=2)
    print(tag.topics)
    # tag1 = Tag(name="Sport")
    # tag2 = Tag(name="Finance")
    # session.add_all(instances=[tag1, tag2])
    # session.commit()
    # session.refresh(instance=tag1)
    # session.refresh(instance=tag2)
    # print(tag1.id, tag1.name)
    # print(tag2.id, tag2.name)
    # tag = session.get(entity=Tag, ident=1)
    # tag.name = "Auto"
    # session.commit()
    # session.delete(instance=tag)
    # session.commit()