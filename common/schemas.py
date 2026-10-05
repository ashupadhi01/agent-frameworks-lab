from pydantic import BaseModel

class SearchResult(BaseModel):
    url: str
    title: str
    content: str


class ResearchReport(BaseModel):
    summary: str
    key_points: list[str]
    sources: list[str]