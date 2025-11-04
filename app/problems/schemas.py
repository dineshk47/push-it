from pydantic import BaseModel, Field


class TwoSum(BaseModel):
    numbers: list[int] = Field(min_length=2)
    target: int
    
