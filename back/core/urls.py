from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workshop.views import ServiceViewSet, MasterViewSet, OrderViewSet, ClientViewSet, BoxViewSet, CarViewSet, public_order_create, home_page

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'masters', MasterViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'boxes', BoxViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/public_order/', public_order_create),
]