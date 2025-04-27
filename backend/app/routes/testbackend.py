from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_connection():
    return {"message": "All set to go"}
