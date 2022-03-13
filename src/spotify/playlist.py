from dataclasses import dataclass
from typing import List

from .track import Track


@dataclass
class Playlist:
    id: str
    name: str
    tracks: List[Track]
