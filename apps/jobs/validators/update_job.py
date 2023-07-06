from typing import Optional
from pydantic import BaseModel

class UpdateJobDTO(BaseModel):
    title: Optional[str]
    description: Optional[str]
    created_by: Optional[int]