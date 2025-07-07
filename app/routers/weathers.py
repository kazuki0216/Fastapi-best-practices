from fastapi import APIRouter, HTTPException
from ..common.input_validation import string_input_validation

router = APIRouter(prefix="/weather")


@router.get("/health")
async def health_check(username: str):
    validation = string_input_validation(username)
    if not validation.result:
        raise HTTPException(status_code=400, detail=validation.details)
    return {"message": f"Hello {username}, the weather is fine."}
