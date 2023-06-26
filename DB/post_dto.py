from dataclasses import dataclass


@dataclass
class PostDto:
    id_: int
    author: str
    title: str
    content: str
    like: int = 0
