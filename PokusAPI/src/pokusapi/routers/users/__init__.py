from fastapi import APIRouter, Depends, HTTPException

from ...commons import get_token_header

# ok next steps : https://fastapi.tiangolo.com/tutorial/bigger-applications/

# app = FastAPI()

# @app.get("/users/{user_id}")
# async def inspect_user(user_id):
#     return {"user_id": user_id}


router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_users_db = {
    "user1": {
      "firstname": "Mark",
      "age": 47,
      "lastname": "Twain"
    },
    "user2": {
      "firstname": "Stendhal",
      "age": 51,
      "lastname": "Stendhal"
    },
    "user3": {
      "firstname": "Howard Philips",
      "age": 34,
      "lastname": "Lovecraft"
    },
    "user4": {
      "firstname": "Saunders",
      "age": 14,
      "lastname": "Mac Lane"
    },
    "userthatisyours": {
      "firstname": "Punky",
      "age": 22,
      "lastname": "Brewster"
    }
}


@router.get("/")
async def inspect_users():
    return fake_users_db


@router.get("/{user_id}")
async def inspect_user(user_id: str):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {
             "age": fake_users_db[user_id]["age"],
             "lastname": fake_users_db[user_id]["lastname"],
             "user_id": user_id
        }


@router.put(
    "/{user_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)

async def update_user(user_id: str):
    if user_id != "userthatisyours":
        raise HTTPException(
            status_code=403, detail=f"You can only update {user_id} - You can only update the User: userthatisyours"
        )
    return {
             "age": fake_users_db[user_id]["age"],
             "lastname": fake_users_db[user_id]["lastname"],
             "user_id": user_id
        }