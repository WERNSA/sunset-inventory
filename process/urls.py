from .views import InventoryViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('inventory', InventoryViewset, basename='inventory')

urlpatterns = router.get_urls()