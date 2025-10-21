from fastapi import FastAPI
from db import SessionDB, Book, select, create_all_talbes

create_all_talbes()

app = FastAPI()

@app.get('/books')
def get_all_books(ssdb: SessionDB):
    books = ssdb.exec(select(Book)).all()

    return [
        book.model_dump()
        for book in books
    ]

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", reload=True)