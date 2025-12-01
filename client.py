import os

import httpx


class AdventOfCodeClient:
    def __init__(self, session_cookie: str | None = None, base_url: str | None = None):
        self.session_cookie = session_cookie or os.getenv("SESSION_COOKIE")
        self.base_url = base_url or os.getenv("BASE_URL", "https://adventofcode.com")
        self._cookies = {"session": self.session_cookie}
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
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
