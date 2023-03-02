from tortoise import Tortoise
from config.utils import resolve


async def init_db():
    db_url = f"{resolve('db.driver')}://{resolve('db.user')}:{resolve('db.password')}@{resolve('db.host')}:{resolve('db.port')}/{resolve('db.name')}"
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ['pkgs.common.models']},
    )

    return Tortoise.get_connection("default")

async def close_db():
    await Tortoise.close_connections()
