import os
import httpx
from dotenv import load_dotenv
from src.logging import logger

load_dotenv(dotenv_path=".env.prod")

async def fetch_mentions(user_name: str):
    api_key = os.getenv("X_API_KEY")

    if not api_key:
        logger.error("Missing X_API_KEY in environment variables.")
        raise ValueError("Missing X_API_KEY")

    headers = {
        "X-API-Key": api_key
    }

    url = f"https://api.twitterapi.io/twitter/user/mentions?userName={user_name}"
    logger.info(f"Fetching mentions for user: {user_name}")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            logger.info(f"Mentions fetched successfully for {user_name}")
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching mentions for {user_name}: {e}")
        raise
