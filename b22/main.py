from sqlmodel import SQLModel, Field, create_engine, Session

engine = create_engine("sqlite:///./db.sqlite2")

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False, min_length=5)
    password: str = Field(nullable=False, min_length=8)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

def get_session():
    with Session(engine) as session:
        yield session

session = next(get_session())
user = User(username='user0034134', password='123456789')
session.add(user)
session.commit()
session.refresh(user)


# xoá user
# session.delete(user)
# session.commit()
# # print(user)

# n = int(input())
# if n%2:
#     print ("EVEN")
# else:
#     print("ODD")