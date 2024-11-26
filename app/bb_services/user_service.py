from app.cc_adapters.repository.user_repository import UserRepository
from app.bb_services.base_service import BaseService


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)