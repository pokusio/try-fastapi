from fastapi import APIRouter, Depends, HTTPException

from ...commons import get_token_header

# ok next steps : https://fastapi.tiangolo.com/tutorial/bigger-applications/

# app = FastAPI()

# @app.get("/books/{book_id}")
# async def inspect_book(book_id):
#     return {"book_id": book_id}


router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_books_db = {
    "tomsawyer": {
      "quote": "The biggest robbers of this world are The Kings, The Nobles, and the preachers",
      "title": "Tom Sawyer",
      "author": "Mark Twain"
    },
    "chartreusedeparme": {
      "quote": "Je croirais assez que le bonheur immoral que l'on trouve à se venger en Italie tient à la force d'imagination de ce peuple",
      "title": "La Chartreuse De Parme",
      "author": "Mark Twain"
    },
    "callofcthulhu": {
      "quote": "I have looked upon all that the universe has to hold of horror, and even the skies of spring and the flowers of summer must ever afterward be poison to me.",
      "title": "The Call of Cthulhu",
      "author": "Howard Philips Lovecraft"
    },
    "catsmaclane": {
      "quote": "Good general theory does not search for the maximum generality, but for the right generality.",
      "title": "Categories for the working mathematician",
      "author": "Saunders Mac Lane"
    },
    "bookthatisyours": {
      "name": "The Blue, The White, The red",
      "title": "The Blue, The White, The red",
      "author": "Punky Brewster"
    }
}


@router.get("/")
async def inspect_books():
    return fake_books_db


@router.get("/{book_id}")
async def inspect_book(book_id: str):
    if book_id not in fake_books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return {
             "title": fake_books_db[book_id]["title"],
             "author": fake_books_db[book_id]["author"],
             "book_id": book_id
        }


@router.put(
    "/{book_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)

async def update_book(book_id: str):
    if book_id != "bookthatisyours":
        raise HTTPException(
            status_code=403, detail=f"You can only updtae {book_id} - You can only update the Book: bookthatisyours"
        )
    return {
             "title": fake_books_db[book_id]["title"],
             "author": fake_books_db[book_id]["author"],
             "book_id": book_id
        }