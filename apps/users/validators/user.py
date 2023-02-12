from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    name: str
    email: EmailStr
    