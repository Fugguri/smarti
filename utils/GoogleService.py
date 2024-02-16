from dacite import from_dict
import asyncio
import gspread
import datetime
from dataclasses import dataclass


class GoogleService:
    def __init__(self) -> None:
        self.gc = gspread.service_account("google_credentials.json")
        self.sh = self.gc.open_by_url(
            "https://docs.google.com/spreadsheets/d/1lleHcwZf8t-RReaoEn2-u0m5-fu0-1YqpJ98tycMM3k/edit#gid=0")

    async def save_lead(self, data: dict):
        print(2)
        try:
            lead = Lead(
                goal=data.get("education_goal"),
                work_with=data.get("work_with"),
                Education_important=data.get("Education_important"),
                work_specific=data.get("work_specific"),
                personal_improvements_goals=data.get(
                    "personal_improvements_goals"),
                budget=data.get("budget"),
                start_education=data.get("start_education"),
                name=data.get("name"),
                phone=data.get("phone"),
                email=data.get("email"),
            )
        except Exception as ex:
            print(ex)

        print(2)

        print(lead)
        ws = self.sh.get_worksheet(0)
        print(ws)
        print(ws.append_row(lead.as_tuple()))


@dataclass
class Lead:
    goal: str = None
    work_with: str = "-"
    Education_important: str = None
    work_specific: str = "-"
    personal_improvements_goals: str = None
    budget: str = None
    start_education: str = None
    name: str = None
    phone: str = None
    email: str = None
    date: str = str(datetime.datetime.strftime(
        datetime.datetime.now(), "%d-%m-%Y, %H:%M:%S"))

    def as_tuple(self):
        return [
            self.goal,
            self.work_with,
            self.Education_important,
            self.work_specific,
            self.personal_improvements_goals,
            self.budget,
            self.start_education,
            self.name,
            self.phone,
            self.email,
            self.date,
        ]


if __name__ == "__main__":

    data = {"education_goal": "новую профессию",
            "work_with": "взрослые",
            "Education_important": "гибкий график",
            "budget": "от 5000 руб/мес",
            "start_education": "в течение месяца", "name": "никита", "phone": "89502213750", "email": "fygguri@icloud"}

    gs = GoogleService()
    asyncio.run(gs.save_lead(data))
