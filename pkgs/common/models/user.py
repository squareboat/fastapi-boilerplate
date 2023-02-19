from tortoise.fields import IntField, CharField, DateTimeField
from tortoise.models import Model


class UserModel(Model):
    id = IntField()
    name = CharField()
    email = CharField()
    password = CharField()
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now=True)

    class PydanticMeta:
        exclude = ["password"]