from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional


engine = create_engine("sqlite:///db.sqlite3")

class AutoId(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)


class User(AutoId, table=True):
    username: str = Field(unique=True, nullable=False)
    password: str = Field(nullable=False)
    def __str__(self):
        return f"{self.username} {self.password}"

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def create_user(username: str, password: str, session: Session):
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
def get_user(username: str, session: Session):
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()
def update_user(username: str, new_password: str, session: Session):
    user = get_user(username, session)
    if user:
        user.password = new_password
        session.add(user)
        session.commit()
        session.refresh(user)
    return user
def delete_user(username: str, session: Session):
    user = get_user(username, session)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False
if __name__ == "__main__":
    session = next(get_session())
    create_db_and_tables()
    new_user = create_user("anhvu12223", "password123", session=session)
    print("User mới được tạo:", new_user)
    print("Tìm user:", get_user("anhvu12223", session))
    update_user("anhvu12223", "newpass456", session)
    print("Sau update:", get_user("anhvu12223", session))
    delete_user("anhvu12223", session)
    print("Sau delete:", get_user("anhvu12223", session))
