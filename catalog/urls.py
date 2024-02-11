from .views import BrandViewset, CategoryViewset, UnitMeasurementViewset, ProductViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('brand', BrandViewset, basename='brand')
router.register('category', CategoryViewset, basename='category')
router.register('unit-measurement', UnitMeasurementViewset, basename='unit-measurement')
router.register('product', ProductViewset, basename='product')

urlpatterns = router.get_urls()