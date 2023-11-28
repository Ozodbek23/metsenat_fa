from fastapi import APIRouter

from  students.routers import router as students_router
from  sponsors.routers import router as sponsors_router
from  users.routers import router as users_router
from  auth.routers import router as auth_router


router = APIRouter(prefix='/api')

router.include_router(students_router)
router.include_router(sponsors_router)
router.include_router(users_router)
router.include_router(auth_router)
