from pydantic import BaseModel

class postcreate(BaseModel):
    title:str
    content:str

class postresponse(BaseModel):
    title:str
    content:str
