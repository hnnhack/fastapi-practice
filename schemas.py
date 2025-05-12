from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
class UserDisplay(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True
        # This will allow us to convert the SQLAlchemy model to a Pydantic model
        # by setting the orm_mode to True.
        # This is useful when we want to return the user data from the database
        # as a response to the client.
