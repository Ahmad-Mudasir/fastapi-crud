# 📚 FastAPI CRUD App - Book Management

This is a simple **CRUD API** built with [FastAPI] using in-memory storage and `UUID` for each book.

You can perform:

- ✅ Add a new book
- 📖 List all books
- 📝 Update a book
- ❌ Delete a book

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- FastAPI
- Uvicorn

### 🧰 Installation

```bash
# Clone the repository
git clone https://github.com/Ahmad-Mudasir/fastapi-crud.git
cd fastapi-crud

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn
```

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

- Visit API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Full Code (main.py)

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    authure: str = Field(min_length=1)
    desc: str = Field(min_length=1)
    rating: float = Field(ge=0, le=5)

Books = []

@app.get("/")
def get_books():
    return Books

@app.post("/")
def create_book(book: Book):
    Books.append(book)
    return book

@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
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
```

---

## 📌 API Reference

### 📖 GET `/`

Fetch all books.

#### ✅ Example Response

```json
[
  {
    "id": "b28c7d27-d0c3-4b0f-b804-e96ea276ac3a",
    "title": "Clean Code",
    "authure": "Robert Martin",
    "desc": "A handbook of agile software craftsmanship",
    "rating": 4.9
  }
]
```

---

### ➕ POST `/`

Add a new book.

#### 📥 Example Request Body

```json
{
  "id": "b28c7d27-d0c3-4b0f-b804-e96ea276ac3a",
  "title": "Clean Code",
  "authure": "Robert Martin",
  "desc": "A handbook of agile software craftsmanship",
  "rating": 4.9
}
```

#### ✅ Example Response

```json
{
  "id": "b28c7d27-d0c3-4b0f-b804-e96ea276ac3a",
  "title": "Clean Code",
  "authure": "Robert Martin",
  "desc": "A handbook of agile software craftsmanship",
  "rating": 4.9
}
```

---

### 📝 PUT `/{book_id}`

Update a book by its `UUID`.

#### 🔗 Example URL

```
PUT /b28c7d27-d0c3-4b0f-b804-e96ea276ac3a
```

#### 📥 Request Body

```json
{
  "id": "b28c7d27-d0c3-4b0f-b804-e96ea276ac3a",
  "title": "Updated Book",
  "authure": "Someone Else",
  "desc": "Updated description",
  "rating": 5
}
```

#### ✅ Response

```json
{
  "id": "b28c7d27-d0c3-4b0f-b804-e96ea276ac3a",
  "title": "Updated Book",
  "authure": "Someone Else",
  "desc": "Updated description",
  "rating": 5
}
```

---

### ❌ DELETE `/{book_id}`

Delete a book by UUID.

#### 🔗 Example URL

```
DELETE /b28c7d27-d0c3-4b0f-b804-e96ea276ac3a
```

#### ✅ Example Response

```json
{
  "detail": "Book deleted"
}
```

---

## 🧪 Test with curl

```bash
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": "b28c7d27-d0c3-4b0f-b804-e96ea276ac3a",
    "title": "Test Book",
    "authure": "John Doe",
    "desc": "Test description",
    "rating": 4.5
  }'
```

---

## 🔑 UUID Generator

To generate UUIDs, run:

```python
import uuid
print(uuid.uuid4())
```

Or visit: https://www.uuidgenerator.net/

---

## 📄 License

Mudasir© 2025 Mudasir
