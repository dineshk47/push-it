from fastapi import APIRouter

from app.problems.router import router as problems_router

api_router = APIRouter()
api_router.include_router(problems_router, prefix="/problems", tags=["Problems"])   
