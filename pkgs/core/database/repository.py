from tortoise import Tortoise

class DBRepository:
    def __init__(self, db: Tortoise) -> None:
        self._db = db
    

    def all(self):
        pass


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