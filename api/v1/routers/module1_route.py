"""
This Router File will serves as the main router link for all module1 objects
"""

from fastapi import APIRouter
from ..controllers.module1.item_controller import router as item_router

router = APIRouter(prefix="/module1")
router.include_router(item_router, prefix="/items",tags=["`items` CRUD"])
