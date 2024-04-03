from abc import ABC, abstractmethod
import os
from threading import Thread


class BaseTokenSaverSource(ABC):
    def __init__(self, source_url: str, project_name: str, project_id: int) -> None:
        super().__init__()
        self.source_url = source_url
        self.project_name = project_name
        self.project_id = project_id

    @abstractmethod
    def _get_record(self, *args, **kwargs):
        ...

    @abstractmethod
    def _save(self, *args, **kwargs):
        ...

    def save(self, tokens: int, project_id: str | int, project_name: str):
        return self.__save(tokens=tokens, project_id=project_id, project_name=project_name)
