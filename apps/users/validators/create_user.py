from pydantic import BaseModel, EmailStr, constr

class CreateUserDTO(BaseModel):
    name: str
    email: EmailStr
    password: constr(max_length=255, min_length=8)