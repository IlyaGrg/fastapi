from fastapi import FastAPI , HTTPException
import uvicorn

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
@app.get("/books")
def read_books():
    return books    


@app.get("/books/{id}")
def get_book(book_id : int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404)
    

if __name__ == "__main__":
    uvicorn.run("main:app" , reload =True)