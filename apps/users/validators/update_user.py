from typing import Optional
from pydantic import BaseModel, EmailStr, constr

class UpdateUserDTO(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[constr(max_length=255, min_length=8)]