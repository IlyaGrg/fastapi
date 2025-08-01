from fastapi import FastAPI , HTTPException
import uvicorn
from pydantic import BaseModel
from math import sqrt

if __name__ == "__main__":
    uvicorn.run("main:app" , reload =True)


app = FastAPI()

books = [
    {
        "id" : 1,
        "title" : "Титька",
        "autor": "Loru"
    },
    {
        "id" : 2,
        "title" : "Попка",
        "autor" : "Gilza"
    }
]
@app.get(
    "/books",
    tags=["Книги"],
    summary="Получить все книги"
)

def get_all_books():
    return books


@app.get(
    "/books/{id}",
    tags=["Одна книга"],
    summary="Получить книгу по id"
)

def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:\
            return book
    raise HTTPException(status_code = 404 , detail = "Книга не найдена")

class NewBook(BaseModel):
    title: str
    autor: str

@app.post(
    "/book",
    tags=["Добавить кнгиу"],
    summary="Добавить свою книгу"
)

def create_book(new_book:NewBook):
    books.append({
        "id" : len(books) + 1,
        "title" : new_book.title,
        "autor" : new_book.autor
    })
    return {"success" : True}