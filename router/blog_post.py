from typing import List, Optional
from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class ImageModel(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    no_of_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: dict[str, str] = {"key1": "value1", "key2": "value2"}
    image: Optional[ImageModel] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version,
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
                   comment_title: int = Query(None, title="Comment Title", description="The Title of the comment", alias="commentTitle", deprecated=True),
                  #  content: str = Body(Ellipsis)):
                   content: str = Body(..., min_length=10, max_length=50, regex="^[a-zA-Z0-9_ ]*$"),
                   v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
                   comment_id: int = Path(..., title="Comment ID", description="The ID of the comment", gt=0, le=1000)
                   ):
                   
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id
        }

def required_functionality():
    return { "message": "Learning FastApi is important" }