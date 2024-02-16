from dataclasses import dataclass
import asyncio
from utils import assistant


@dataclass
class User:
    id: int
    username: str


@dataclass
class Message:
    text: str
    from_user: User


user = User(123123, "fdsfds")

message1 = Message(text="привет", from_user=user)
message2 = Message(text="подобрать", from_user=user)

chat_id1 = 1342
chat_id2 = 1234
chat_id3 = 3431
chat_id4 = 6453


async def test_assistant1():
    data = [await assistant.request(message=message1, chat_id=chat_id1),
            await assistant.request(message=message2, chat_id=chat_id1)]


async def test_assistant2():
    data = [await assistant.request(message=message1, chat_id=chat_id2),
            await assistant.request(message=message2, chat_id=chat_id2)]


async def test_assistant3():
    data = [await assistant.request(message=message1, chat_id=chat_id3),
            await assistant.request(message=message2, chat_id=chat_id3)]


async def test_assistant4():
    data = [await assistant.request(message=message1, chat_id=chat_id4),
            await assistant.request(message=message2, chat_id=chat_id4)]


async def test():
    result = []
    result.append(await test_assistant1())
    result.append(await test_assistant2())
    result.append(await test_assistant3())
    result.append(await test_assistant4())
    print(result)
asyncio.run(test())
