from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import CategoryView, ProductView, OrderView

router = DefaultRouter()
router.register('category', CategoryView, basename='category')
router.register('product', ProductView, basename='product')
router.register('order', OrderView, basename='order')

urlpatterns = router.urls
