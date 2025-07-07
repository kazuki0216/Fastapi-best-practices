from fastapi import APIRouter

router = APIRouter()


@router.get("/cafe/health")
async def health_check(username: str):
    return {"message": f"Hello {username}, today's specialty is cafe ole."}
