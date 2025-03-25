from fastapi import FastAPI, Query, HTTPException
from src.components.twitter_mentions_service import fetch_mentions

app = FastAPI(
    title="Twitter Mentions Service",
    version="1.0.0"
)

@app.get("/mentions")
async def get_mentions(
    userName: str = Query(..., description="Twitter @username")
):
    try:
        data = await fetch_mentions(userName)
        tweet_ids = [tweet["id"] for tweet in data.get("tweets", [])]
        return {
            "mention": userName,
            "tweet_ids": tweet_ids
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))