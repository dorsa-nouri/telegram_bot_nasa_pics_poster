from nasa_channel_poster import post
import time
import os
from dotenv import load_dotenv
from asyncio import run

load_dotenv(".env")


async def main(bot_token: str, chat_id: int, nasa_api_token: str, sleep_time: int):
    while True:
        try:
            await post(
                bot_token=bot_token,
                chat_id=chat_id,
                nasa_api_token=nasa_api_token,
            )
        except:
            pass
        finally:
            time.sleep(sleep_time)


if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHANNEL_CHAT_ID = os.getenv("CHANNEL_CHAT_ID")
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    # SLEEP_TIME = 10 * 60  # seconds
    SLEEP_TIME = 15  # seconds
    run(
        main(
            bot_token=BOT_TOKEN,
            chat_id=CHANNEL_CHAT_ID,
            nasa_api_token=NASA_API_KEY,
            sleep_time=SLEEP_TIME,
        )
    )
