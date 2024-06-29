"""
This Router File will serves as the main router link for this api
"""

from fastapi import APIRouter
from .module1_route import router as module1_router

router = APIRouter(prefix="/api/v1")
router.include_router(module1_router)