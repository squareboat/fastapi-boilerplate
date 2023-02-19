from tortoise import Tortoise
from config.utils import resolve

class Database:
    async def __init__(self) -> None:
        self.db_url = f"{resolve('db.driver')}://{resolve('db.user')}:{resolve('db.password')}@{resolve('db.host')}:{resolve('db.port')}/{resolve('db.name')}"
        await Tortoise.init(
            db_url=self.db_url,
            modules={"models": ['pkgs.common.models']},
        )

    async def __del__(self) -> None:
        await Tortoise.close_connections()

