"""
This Router File will serves as the main router link for all module1 objects
"""

from fastapi import APIRouter
from api.v1.controllers.admin.item_controller import router as item_router
from api.v1.controllers.admin.user_controller import router as user_router
from api.v1.controllers.admin.role_controller import router as role_router

router = APIRouter(prefix="/admin")
router.include_router(item_router, prefix="/items",tags=["admin/items CRUD"])
router.include_router(user_router, prefix="/users",tags=["admin/users CRUD"])
router.include_router(role_router, prefix="/roles",tags=["admin/roles CRUD"])
