from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.aa_domain.model.user import User
from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, User)