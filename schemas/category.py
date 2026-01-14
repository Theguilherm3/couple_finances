from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=60, examples=["Alimentação"])


class CategoryOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
