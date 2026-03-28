from fastapi import APIRouter

router = APIRouter(
    prefix = "notebooks",
    tags = "Notebooks"
)

@router.get()
async def get_notebooks():
    