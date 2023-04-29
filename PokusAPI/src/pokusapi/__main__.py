"""Pokus API."""

import uvicorn

# if __name__ == "__main__":
#     main(prog_name="pokusapi")  # pragma: no cover


from fastapi import Depends, FastAPI

from .commons import get_query_token, get_token_header
from .internals import admin
from .routers import books, users
# from .routers import books

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(books.router)
app.include_router(users.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot for the pokusapi Admin module"}},
)


@app.get("/")
async def root():
    return {"message": "Hello PokusAPI Bigger Application !"}


def start():
    """Launched with `poetry run start` at root level"""
    # uvicorn.run("pokusapi.__main__:main", host="0.0.0.0", port=8000, reload=True)
    # uvicorn.run("pokusapi.routers.books:app", host="0.0.0.0", port=8000, reload=False)
    uvicorn.run("pokusapi.__main__:app", host="0.0.0.0", port=8000, reload=False)
    # uvicorn.run("pokusapi:app", host="0.0.0.0", port=8000, reload=True)
