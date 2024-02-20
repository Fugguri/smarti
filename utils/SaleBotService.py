

import requests
import json


class SalebotService:
    def __init__(self) -> None:
        self.base_url = 'https://chatter.salebot.pro/api/{api_key}/{action}'

    async def sync_save_variables(self, api_key, client_id, variables: dict):
        params = {"client_id": client_id, "variables": variables}
        url = self.base_url.format(api_key=api_key, action="save_variables")
        req = requests.post(url, json=params)
        return req

    def save_variables(self, api_key, client_id, variables: dict):
        params = {"client_id": client_id, "variables": variables}
        url = self.base_url.format(api_key=api_key, action="save_variables")
        req = requests.post(url, json=params)
        return req

    async def sync_send_message(self, api_key, client_id, message: str):
        params = {"message": message, "client_id": client_id}
        url = self.base_url.format(api_key=api_key, action="message")
        print(url)
        req = requests.post(url, json=params)
        print(req.text)
        return req

    def send_message(self, api_key, client_id, message: str):

        params = {"message": message, "client_id": client_id}
        url = self.base_url.format(api_key=api_key, action="message")
        req = requests.post(url, json=params)
        return req
