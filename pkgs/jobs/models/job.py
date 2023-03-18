from tortoise.fields import IntField, CharField, DatetimeField, TextField, OneToOneField
from pkgs.core.database import BaseModel

class JobModel(BaseModel):
    id = IntField(pk=True)
    uuid = CharField(max_length=255)
    title = CharField(max_length=255)
    description = TextField()
    created_by = OneToOneField('models.UserModel')
    created_at = DatetimeField(auto_now=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        table="jobs"