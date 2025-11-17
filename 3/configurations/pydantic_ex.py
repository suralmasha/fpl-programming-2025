from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime

def print_row(label, value, width=25):
    print(f'{label.ljust(width)} {value}')

# ----------------------------------------
# Простая модель с типами и дефолтами
# ----------------------------------------
class User(BaseModel):
    id: int
    name: str = 'Anonymous'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

user = User(id='123', friends=['1', 2, 3])
print_row('Auto-conversion', user)

# ----------------------------------------
# Вложенные модели
# ----------------------------------------
class Address(BaseModel):
    street: str
    city: str

class Profile(BaseModel):
    user: User
    address: Address

profile = Profile(
    user={'id': 42, 'name': 'Alice'},
    address={'street': 'Main St', 'city': 'Moscow'}
)
print_row('Nested models', profile)

# ----------------------------------------
# Валидация
# ----------------------------------------
class Product(BaseModel):
    name: str
    price: float
    discount: float = 0.0

    @field_validator('discount')
    def discount_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('discount must be non-negative')
        return v

product = Product(name='Laptop', price=1000, discount=50)
print_row('Validation', product)

# ----------------------------------------
# Сериализация
# ----------------------------------------
print_row('Serialization dict', product.model_dump())
print_row('Serialization json', product.model_dump_json())

# ----------------------------------------
# Преобразование данных при валидации
# ----------------------------------------
class Item(BaseModel):
    name: str
    price: float

    @field_validator('price', mode='before')
    def convert_price(cls, v):
        if isinstance(v, str):
            return float(v.replace(',', '.').replace(' руб', ''))
        return v

item = Item(name='Book', price='12,5 руб')
print_row('Custom conversion', item)

# ----------------------------------------
# Field с ограничениями
# ----------------------------------------
class Employee(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=18, le=70)
    email: str

emp = Employee(name='Bob', age=30, email='bob@example.com')
print_row('Field with restrictions', emp)
