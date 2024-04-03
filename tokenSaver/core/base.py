import os
from abc import ABC, abstractmethod
from threading import Thread
from typing import Iterable, List, Dict, Tuple

from tokenSaver.core.Sources import BaseTokenSaverSource
from .Sources import BaseTokenSaverSource

# import logging


class BaseTokenSaver(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add_source(self, source: BaseTokenSaverSource):
        ...

    @abstractmethod
    def _save_tokens_usage(self, project_id: int):
        ...


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class DefaultTokenSaver(BaseTokenSaver):

    def __init__(self) -> None:
        super().__init__()
        self.sources: Dict[int: Tuple[BaseTokenSaverSource]] = dict()
        # self.loglever = logging.DEBUG
        # # self.logging = logging
        # self.logging.basicConfig(
        #     level=self.loglever,
        #     format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        #     filename="logs/token_saver_logs.log"
        # )

    def save_tokens_usage(self, tokens: int, project_id: str | int = None, project_name: str = None):
        return self._save_tokens_usage(tokens=tokens, project_id=project_id, project_name=project_name)

    async def asave_tokens_usage(self, tokens: int, project_id: str | int = None, project_name: str = None):
        return self._save_tokens_usage(tokens=tokens, project_id=project_id, project_name=project_name)

    def _save_tokens_usage(self, tokens: int, project_id: str | int, project_name: str):
        # import multiprocessing
        # cores: int = multiprocessing.cpu_count()
        # TODO: should i rewrite to parallel source execution based on cpu count

        sources = self.sources.get(project_id)

        if not sources:
            # self.logging.debug("Sources was newer added yet")
            print(bcolors.FAIL+"Sources was newer added yet")
            return
        for source in sources:
            if not isinstance(source, BaseTokenSaverSource):
                raise Exception(
                    "source is not an instance of a class: BaseTokenSaverSource ")
            source.save(tokens=tokens, project_id=project_id,
                        project_name=project_name)

    def add_source(self, project_id: int, source: BaseTokenSaverSource):
        project = self.sources.get(project_id)
        if not project:
            self.sources.setdefault(project_id, [])

        self.sources[project_id].append(source)
        # self.logging.debug(
        # f"Sources added for projectID: {project_id} - {source}")
        return
