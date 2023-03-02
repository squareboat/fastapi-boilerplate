from tortoise.fields import IntField, CharField, DatetimeField
from tortoise.models import Model

class UserModel(Model):
    id = IntField(pk=True)
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    password = CharField(max_length=255)
    created_at = DatetimeField(auto_now=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        table="users"