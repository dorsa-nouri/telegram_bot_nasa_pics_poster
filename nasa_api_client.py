import requests


class NASAApodAPIClient:
    def __init__(self, api_key, url) -> None:
        self.api_key = api_key
        self.url = url

    def get_data_by_date(self, date: str) -> dict:
        params = {"api_key": self.api_key, "date": date}
        return requests.get(self.url, params=params).json()

    def get_data_by_range(self, start_date: str, end_date: str) -> list[dict]:
        params = {
            "api_key": self.api_key,
            "start_date": start_date,
            "end_date": end_date,
        }
        return requests.get(self.url, params=params).json()

    def get_random_data(self, count: int) -> list[dict]:
        params = {
            "api_key": self.api_key,
            "count": count,
        }
        return requests.get(self.url, params=params).json()

    def download_image(self, url: str, path: str):
        image_res = requests.get(url)
        with open(path, "wb") as file:
            file.write(image_res.content)