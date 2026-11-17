from fastapi import APIRouter, HTTPException

router=APIRouter(
    prefix="/registration",
    tags=["auth"]
)

@router.post("/", status_code=201)
async def create_new_user()