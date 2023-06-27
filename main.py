from fastapi import FastAPI 
#app = FastAPI()
#@app.get("/")
#def root():
 #   return {"message": "hello wordpython -m uvicorn main:app --reload"}
from pydantic import BaseModel

books = []

class Book(BaseModel):
    ano : str
    titulo : str

class Title(BaseModel):
    titulo : object

app = FastAPI()

@app.get("/")
def root():
   if books == []:
      return  {"message": "nenhum livro encontrado"}
   else:
      return books
   
@app.post("/new")
def create_book(book: Book):
    books.append(book)
    return book

   
@app.delete("/")
def delete_book(params: Title):
   for book in books:
      if book.titulo == params.titulo:
         index = books.index(book)
         books.pop(index)
      