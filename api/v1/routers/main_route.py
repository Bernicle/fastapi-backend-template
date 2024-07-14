"""
This Router File will serves as the main router link for this api
"""

from fastapi import APIRouter
from .module1_route import router as module1_router
from ..controllers.authentication_controller import router as authentication_router

router = APIRouter(prefix="/api/v1")
router.include_router(authentication_router)
router.include_router(module1_router)