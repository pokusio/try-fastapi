from typing import Annotated

from fastapi import Header, HTTPException

# ---
# $ # curl -H "X-Token: pokus-super-secret-token" -X GET -ivvv http://127.0.0.1:8000/books/?token=jessica | tail -n 1 | jq .
async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "pokus-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# ---
# $ # curl -H "X-Token: pokus-super-secret-token" -X GET -ivvv http://127.0.0.1:8000/users/?token=jessica | tail -n 1 | jq .
async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
