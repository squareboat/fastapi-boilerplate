from tortoise.fields import IntField, CharField, DatetimeField, TextField, ForeignKeyField
from pkgs.core.database import BaseModel

class JobModel(BaseModel):
    id = IntField(pk=True)
    uuid = CharField(max_length=255)
    title = CharField(max_length=255)
    description = TextField()
    created_by = ForeignKeyField('models.UserModel', related_name="jobs")
    created_at = DatetimeField(auto_now=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        table="jobs"