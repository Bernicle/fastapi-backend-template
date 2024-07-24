"""
This Router File will serves as the main router link for all module1 objects
"""

from fastapi import APIRouter
from api.v1.controllers.admin.item_controller import router as item_router
from api.v1.controllers.admin.user_controller import router as user_router

router = APIRouter(prefix="/module1")
router.include_router(item_router, prefix="/items",tags=["`items` CRUD"])
router.include_router(user_router, prefix="/users",tags=["`users` CRUD"])
