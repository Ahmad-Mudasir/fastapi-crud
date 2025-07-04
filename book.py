from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID  # ✅ use UUID, not uuid4

app = FastAPI()
class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    authure: str = Field(min_length=1)
    desc: str = Field(min_length=1)
    rating: float = Field(ge=0, le=5)
    
Books= []
    
@app.get("/")
def get_books():
        return Books
    
@app.post("/")
def create_book(book: Book):
        Books.append(book)
        return book
    
    
    
@app.put("/{book_id}")
def update_book(book_id:    UUID, book: Book):
    for i, b in enumerate(Books):
        if b.id == book_id:
            Books[i] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")    


@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    for i, b in enumerate(Books):
        if b.id == book_id:
            del Books[i]
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")