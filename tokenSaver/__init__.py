from .core.Sources import GoogleSheetsSource
from .core.base import DefaultTokenSaver

token_saver = DefaultTokenSaver()

gsource = GoogleSheetsSource(
    project_id=1,
    project_name="Смартик",
    source_url="https://docs.google.com/spreadsheets/d/1aeARfwy2Zdk8GLWNK14CWDV0iOybd5B_GID0M3wxHlU/edit#gid=0")

token_saver.add_source(1, gsource)
