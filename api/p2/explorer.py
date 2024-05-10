from fastapi import APIRouter

router = APIRouter()

router.get("/")
def top():
    return "top explorer endpoint"