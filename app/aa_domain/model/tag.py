from sqlmodel import Field

from .base_model import BaseModel


# модель таблицы "тэг"
class Tag(BaseModel, table=True):
    user_token: str = Field()

    name: str = Field(unique=True)
    description: str = Field(default=None, nullable=True)