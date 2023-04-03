from tortoise.fields import IntField, CharField, DatetimeField, ReverseRelation
from pkgs.core import BaseModel
from pkgs.jobs.models import JobModel

class UserModel(BaseModel):
    id = IntField(pk=True)
    uuid = CharField(max_length=255)
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    password = CharField(max_length=255)
    jobs = ReverseRelation["JobModel"]
    created_at = DatetimeField(auto_now=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        table="users"