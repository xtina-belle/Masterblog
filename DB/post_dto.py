from dataclasses import dataclass


@dataclass
class PostDto:
    """represents a post"""
    id_: int
    author: str
    title: str
    content: str
    like: int = 0
