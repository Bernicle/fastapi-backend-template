"""
This Router File will serves as the main router link for this api
"""

from fastapi import APIRouter
from api.v1.routers.admin_route import router as admin_router
from api.v1.controllers.authentication_controller import router as authentication_router

router = APIRouter(prefix="/api/v1")
router.include_router(authentication_router,tags=["LOGIN"])
router.include_router(admin_router)