import asyncio
import os
from dotenv import load_dotenv
from src.components.twitter_mentions_service import fetch_mentions

# Load .env.prod
load_dotenv(dotenv_path=".env.prod")

if __name__ == "__main__":
    async def test():
        data = await fetch_mentions("id_bachao")
        tweet_ids = [tweet["id"] for tweet in data.get("tweets", [])]
        print("Tweet IDs:", tweet_ids)

    asyncio.run(test())
