from pydantic import BaseModel


class Pattern(BaseModel):
    pattern: str
    description: str = None
