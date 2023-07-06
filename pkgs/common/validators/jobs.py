from pydantic import BaseModel

class CreateJob(BaseModel):
    title: str
    description: str
    created_by_id: int