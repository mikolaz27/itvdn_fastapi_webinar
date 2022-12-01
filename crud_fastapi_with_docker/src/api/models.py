from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
    created_by: str = Field(..., min_length=3, max_length=50)


class PostDB(PostSchema):
    id: int
