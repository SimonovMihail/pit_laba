from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workshop.views import ServiceViewSet, MasterViewSet, OrderViewSet, ClientViewSet, BoxViewSet, CarViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'masters', MasterViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'boxes', BoxViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]