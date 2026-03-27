from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    id: int = Field(...)
    nome: str = Field(..., min_length = 3)
    gmail: EmailStr
    telefone: str
    nivelPerm: int
    