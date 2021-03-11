from rest_framework import routers
from .views import OrderViewSet

router = routers.SimpleRouter()
router.register('orders', viewset=OrderViewSet)
urlpatterns = router.urls
