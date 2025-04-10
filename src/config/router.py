from core.comesc import views
from core.usuario.router import router as user_router
from core.uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'address', views.AddressViewSet)
router.register(r'color', views.ColorViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'material', views.MaterialViewSet)
router.registry.extend(user_router.registry)
router.registry.extend(uploader_router.registry)