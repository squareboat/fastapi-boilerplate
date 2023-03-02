from tortoise import Tortoise
from tortoise.models import Model

class DBRepository:
    def __init__(self, db: Tortoise, model: Model) -> None:
        self._db = db
        self._model = model
    

    async def all(self):
        return await self._model.all(using_db=self._db).values()


    def create(self):
        pass

    def create_or_update(self):
        pass

    def get_where(self):
        pass

    def exists(self):
        pass

    def first_where(self):
        pass

    def bulk_insert(self):
        pass
    
    def update(self):
        pass

    def delete_where(self):
        pass