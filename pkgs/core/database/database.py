from glob import glob
from tortoise import Tortoise
from config.utils import resolve


async def init_db():
    db_url = f"{resolve('db.driver')}://{resolve('db.user')}:{resolve('db.password')}@{resolve('db.host')}:{resolve('db.port')}/{resolve('db.name')}"
    await Tortoise.init(
        db_url=db_url,
        modules={"models": list(filter(lambda x: not x.endswith('__init__') ,map(lambda x: '.'.join(x.split('/')), [i[:-3] for i in glob('pkgs/**/models/*.py')])))}
    )

    return Tortoise.get_connection("default")
