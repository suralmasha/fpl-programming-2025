from pydantic import BaseModel


class DBUser(BaseModel):
    name: str
