

import asyncio
import requests
import aiohttp


class SalebotService:
    def __init__(self) -> None:
        self.base_url = 'https://chatter.salebot.pro/api/{api_key}/{action}'

    async def sync_save_variables(self, api_key, client_id, variables: dict):

        async with aiohttp.ClientSession() as session:
            params = {"client_id": client_id, "variables": variables}
            url = self.base_url.format(
                api_key=api_key,
                action="save_variables")

            async with session.post(url, json=params) as req:
                print(await req.text())
                return req

    def save_variables(self, api_key, client_id, variables: dict):
        params = {"client_id": client_id, "variables": variables}
        url = self.base_url.format(api_key=api_key, action="save_variables")
        req = requests.post(url, json=params)
        print(req.content)
        return req

    async def sync_send_message(self, api_key, client_id, message: str):
        async with aiohttp.ClientSession() as session:
            params = {"message": message, "client_id": client_id}
            url = self.base_url.format(api_key=api_key, action="message")
            print(url)
            async with session.post(url, data=params) as req:
                print(await req.text())
                return req

    def send_message(self, api_key, client_id, message: str):

        params = {"message": message, "client_id": client_id}
        url = self.base_url.format(api_key=api_key, action="message")
        req = requests.post(url, json=params)
        return req


if __name__ == "__main__":
    sale = SalebotService()
