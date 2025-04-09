from core.comesc import views
from core.usuario.router import router as user_router
from core.uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.registry.extend(user_router.registry)
router.registry.extend(uploader_router.registry)