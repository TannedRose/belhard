from lesson11 import *
from sqlalchemy import select, update, delete, insert, and_, any_, or_, all_

# with session_maker() as session:
    # session.scalars()
    # session.execute().scalars()
    # session.scalar()
    # session.execute().scalar()

# stmt = select(Topic).order_by(Topic.date_created.desc())
# stmt = stmt.limit(2).offset(1)
# stmt = stmt.filter(or_(Topic.id >= 2, ~Topic.title.incontains("new")))
# print(stmt)


q = select(chat).join(ChatRelation)

MMMMMMMMMMMMMM