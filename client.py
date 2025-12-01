import os

import httpx
from dotenv import load_dotenv

load_dotenv()


class AdventOfCodeClient:
    def __init__(self, session_cookie: str | None = None, base_url: str | None = None):
        self.session_cookie = session_cookie or os.getenv("SESSION_COOKIE")
        self.base_url = base_url or os.getenv("BASE_URL")
        self._cookies = {"session": self.session_cookie}
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        }

    def get_input(self, year: int, day: int) -> str:
        url = f"{self.base_url}/{year}/day/{day}/input"

        response = httpx.get(
            url,
            cookies=self._cookies,
            headers=self._headers,
            timeout=120,
        )
        response.raise_for_status()
        return response.text
