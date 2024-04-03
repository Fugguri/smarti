from dataclasses import dataclass


@dataclass
class RecordRow:
    name: str
    id: int
    token3: int
    token4: int
    embeding: int
    row: int | str
