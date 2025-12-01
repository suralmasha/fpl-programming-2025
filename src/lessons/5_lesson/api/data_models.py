from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class User(BaseModel):
    name: str
    age: int
