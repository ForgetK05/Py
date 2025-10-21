from sqlmodel import (
    SQLModel,
    create_engine,
    Session,
    select,
    Field,
)

engine = create_engine('sqlite:///./db.sqlite3')

class IdAutoField(SQLModel):
    id: int = Field(default=None, primary_key=True)


class User(IdAutoField, table=True):
    username: str = Field(unique=True, nullable=False, min_length=5)
    password: str = Field(nullable=False, min_length=8)

class AuthorBook(IdAutoField, table=True):
    user_id: int
    book_id: int

class Book(IdAutoField, table=True):
    name: str
    country: str

def create_all_tables():
    SQLModel.metadata.create_all(engine)

create_all_tables()

def get_session():
    with Session(engine) as session:
        yield session




session = next(get_session())

# user = User(username='user0001', password='123456789')
# session.add(user)
# session.commit()
# session.refresh(user)


# Cập nhật
# user = session.exec(select(User).where(User.id==1)).one()

# user.username = 'user0002'
# session.add(user)
# session.commit()
# session.refresh(user)

# session.delete(user)
# session.commit()


book = Book(name='Harry Potter', country='US')
user = User(username='user00013', password='123456789')
session.add_all([book, user])
session.commit()
session.refresh(book)
session.refresh(user)


author_book = AuthorBook(user_id=user.id, book_id=book.id)
session.add(author_book)
session.commit()
session.refresh(author_book)