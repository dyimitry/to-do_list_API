from fastapi import APIRouter
from app.endpoints.user import router as user_router
from app.endpoints.to_do_list import router as to_do_list_router

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(to_do_list_router)

