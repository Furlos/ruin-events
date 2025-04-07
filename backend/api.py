from fastapi import APIRouter
from User.api import router as user_router
from Events.api import router as event_router

router = APIRouter()
router.include_router(user_router, prefix="/users")
router.include_router(event_router, prefix="/events")