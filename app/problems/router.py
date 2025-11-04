from fastapi import APIRouter
from app.problems.schemas import TwoSum


router = APIRouter()

@router.post("/two-sum")
def two_sum(payload: TwoSum):
    numbers, target = payload.numbers, payload.target
    left = 0 
    right = len(numbers)-1
    print(numbers, target)
    while left < right:
        add = numbers[left] + numbers[right]
        if add == target:
            return {"indices": [left+1, right+1]}
        elif add < target:
            left += 1
            print(left, right)  
        else:
            right -= 1
    return {"error": "No valid pair found"}

    