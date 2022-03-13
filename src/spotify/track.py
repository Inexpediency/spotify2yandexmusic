from dataclasses import dataclass
from typing import List

from .artist import Artist


@dataclass
class Track:
    id: str
    title: str
    artists: List[Artist]
