from pydantic import BaseModel

class CreateJobDTO(BaseModel):
    title: str
    description: str
    created_by_id: int