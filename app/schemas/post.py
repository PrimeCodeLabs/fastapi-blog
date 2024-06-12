from pydantic import BaseModel

class PostBase(BaseModel):
    text: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True 
