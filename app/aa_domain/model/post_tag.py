from sqlmodel import Field

from .base_model import BaseModel


# модель таблицы связи многие-ко-многим между сущностями "пост" и "тэг"
class PostTag(BaseModel, table=True):
    __tablename__ = "post_tag"
    post_id: int = Field(foreign_key="post.id", primary_key=True, index=True, nullable=False)
    tag_id: int = Field(foreign_key="tag.id", primary_key=True, index=True, nullable=False)