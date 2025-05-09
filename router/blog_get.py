from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional


router = APIRouter(
  prefix="/blog",
  tags=["blog"]
)

@router.get("/")
def index():
    return {"message": "Hello, World!"}

@router.get(
        "/all",
        summary="Get all blogs",
        description="This endpoint retrieves all blogs with pagination support.",
        response_description="A list of all blogs"
        )

def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}

@router.get("/{id}/comments/{comment_id}", tags=["comments"])
def get_blog_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates getting a blog comment by blog ID and comment ID.

    - **id**: mandatory path parameter.
    - **comment_id**: mandatory path parameter.
    - **valid**: Optional query parameter.
    - **username**: Optional query parameter.
    """
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get("/type/{type}")
def get_blog_by_type(type: BlogType):
    return {"message": f"Blog type {type.value}"}

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Blog not found"}
    elif id == 10:
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"message": "Blog is forbidden"}
    else:
        response.status_code = status.HTTP_200_OK
    return {"message": f"Blog with id {id}"}
