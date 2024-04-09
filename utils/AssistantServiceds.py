from tokenSaver import token_saver
import json
from .SaleBotService import SalebotService
import re
from openai import OpenAI
import os
import asyncio
import httpx
proxy_url = "http://9gfWr9:g0LSUy@131.108.17.194:9799/"
salebot = SalebotService()


class AssistantService:

    def __init__(self, api_key, model_name="gpt-3.5-turbo-16k"):
        os.environ['OPENAI_API_KEY'] = api_key
        os.environ['HTTP_PROXY'] = proxy_url
        os.environ['HTTPS_PROXY'] = proxy_url
        # Инициализация OpenAI с использованием прокси
        self.users_threads = dict()
        self.token_saver = token_saver

        self.openai = OpenAI(api_key=api_key,
                             http_client=httpx.Client(
                                 proxies=proxy_url,
                                 transport=httpx.HTTPTransport(
                                     local_address="0.0.0.0"),
                             ),
                             # model_name=model_name,
                             # http_client=http_client,
                             # system_prompt=promt
                             )

        self.assistant = self.openai.beta.assistants.retrieve(
            "asst_2XNAfX7weQ5iGFbWSAUOt8p4")
        print(self.assistant.name)
        self.is_run_active = bool

    def submin_function(self, thread, run, call):
        r = self.openai.beta.threads.runs.submit_tool_outputs(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=[
                {
                    "tool_call_id": call.id,
                    "output": "true",
                },
            ]
        )
        return r

    def __get_thread(self, chat_id):
        print(1)
        thread = self.users_threads.get(chat_id, None)
        if not thread:
            self.users_threads[chat_id] = self.openai.beta.threads.create()
            thread = self.users_threads[chat_id]
        return thread

    async def request(self, message, chat_id, start: bool = False, api_key=None):
        thread = self.__get_thread(chat_id=chat_id)
        print(2)
        ready = False
        while not ready:
            try:
                user_message = self.openai.beta.threads.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content=message.text
                )
                ready = True

            except Exception as ex:
                print(ex)
                await asyncio.sleep(2)

        print(3)

        run = self.openai.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant.id,
        )
        if start:
            print("start")
            return

        status = self.openai.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        ).completed_at
        print(5)
        counter = 1
        while status == None:
            retrieve = self.openai.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            print(counter)
            tokens = retrieve.usage

            counter += 1
            action = retrieve.required_action
            if action:
                data = action.submit_tool_outputs.tool_calls[0].function.arguments
                json_acceptable_string = data.replace("'", "\"")
                lead = json.loads(json_acceptable_string)
                print(lead)
                await salebot.sync_save_variables(api_key=api_key, client_id=chat_id, variables=lead)
                # await message.bot.send_message(-1002137202749, action.submit_tool_outputs.tool_calls[0].function.arguments)
                # await google.save_lead(lead)
                print(self.submin_function(
                    thread, run, action.submit_tool_outputs.tool_calls[0]))

            status = retrieve.completed_at
            await asyncio.sleep(2)

            if not tokens:
                continue

            await self.token_saver.asave_tokens_usage(
                tokens=int(tokens.total_tokens.real), project_id=1, project_name="Смартик")

        messages = self.openai.beta.threads.messages.list(
            thread_id=thread.id
        )
        answer = self.__get_answer_from_messages(messages, user_message.id)
        print(answer)
        if not answer:
            return messages.data[0].content[0].text.value
        return answer

    def __get_answer_from_messages(self, messages, user_message_id):
        index = 0
        for message in messages:
            if message.id == user_message_id:
                return messages.data[index-1].content[0].text.value.replace("【11†источник】", "").replace("**", "").replace("【17†source】", "")
            index += 1
        return None
