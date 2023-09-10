from pydantic import BaseModel

class Task (BaseModel):
    id: int
    task : str
    completed :bool 
