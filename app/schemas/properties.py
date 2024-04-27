from typing import Optional
from pydantic import BaseModel, Field, StringConstraints

class SoldProperties(BaseModel):
    location: str  
    pageNumber:Optional [int] = 1
    


