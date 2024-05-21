from telegram import Bot
import nasa_api_client


async def post(bot_token: str, chat_id: int, nasa_api_token: str) -> bool:
    bot = Bot(token=bot_token)
    nasa_client = nasa_api_client.NASAApodAPIClient(
        api_key=nasa_api_token,
        url="https://api.nasa.gov/planetary/apod",
    )
    nasa_data = nasa_client.get_random_data(1)[0]
    if nasa_data["media_type"] == "image":
        pic_url = nasa_data["url"]
        pic_date = nasa_data["date"]
        title = nasa_data["title"]
        explanation = nasa_data["explanation"]
        nasa_client.download_image(pic_url, "image.jpg")
        converted_date = pic_date.replace("-", "")[2:]
        page_url = f"https://apod.nasa.gov/apod/ap{converted_date}.html"
        caption = f"<a href='{page_url}'><b>{title}</b></a>\n{pic_date}\n\n{explanation}\n\n<a href='https://t.me/drops2024new'>@Dr😳ps</a>"
        await bot.send_photo(
            chat_id=chat_id, photo="image.jpg", caption=caption, parse_mode="HTML"
        )
        return True
    else:
        return False
