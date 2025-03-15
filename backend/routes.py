from fastapi import APIRouter, Request
import requests
import os

router = APIRouter()

GITHUB_TOKEN_NAME = os.getenv("GITHUB_TOKE_NAME")  # Make sure this is set with the right scopes
HEADERS = {"Authorization": f"token {GITHUB_TOKEN_NAME}"}

@router.post("/github/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    print(payload)
    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "issues":
        issue_data = payload["issue"]
        action = payload["action"]
        # Use the API URL for posting comments
        comments_url = issue_data["comments_url"]
        user = issue_data["user"]["login"]

    
    return {"status": "ok"}


