from fastapi import FastAPI, Header, Path, Query
from datetime import datetime
from typing import Optional

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(
    user_id: int = Path(..., description="User ID (must be an integer)"),
    timestamp: Optional[str] = Query(None, description="Optional timestamp"),
    x_client_version: str = Header(..., description="Client version header"),
):
    if not timestamp:
        timestamp = datetime.utcnow().isoformat()

    return {
        "user_id": user_id,
        "timestamp": timestamp,
        "x_client_version": x_client_version,
        "message": f"Hello, user {user_id}!"
    }
