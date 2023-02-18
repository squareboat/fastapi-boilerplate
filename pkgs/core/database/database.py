from tortoise import Tortoise

class Database:
    async def __init__(self, db_url: str) -> None:
        self.db_url = f'{"DB_TYPE"}://{"USERNAME"}:{"PASSWORD"}@{"HOST"}:{"PORT"}/{"DB_NAME"}'
        await Tortoise.init(
            db_url=self.db_url,
            modules={"models": ['pkgs.models']},
        )

    async def __del__(self) -> None:
        await Tortoise.close_connections()

