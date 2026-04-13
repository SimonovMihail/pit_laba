from rest_framework import viewsets
from .models import Services, Masters, Orders, Clients, Boxes, Cars
from .serializers import (
    ServiceSerializer, MasterSerializer, OrderSerializer,
    ClientSerializer, BoxSerializer, CarSerializer
)

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """Эндпоинт для просмотра услуг (Только чтение)"""
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class MasterViewSet(viewsets.ReadOnlyModelViewSet):
    """Эндпоинт для просмотра мастеров (Только чтение)"""
    queryset = Masters.objects.all()
    serializer_class = MasterSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """Эндпоинт для управления заказами (Полный доступ)"""
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """Эндпоинт для работы с клиентами"""
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

class BoxViewSet(viewsets.ModelViewSet):
    """Эндпоинт для работы с боксами"""
    queryset = Boxes.objects.all()
    serializer_class = BoxSerializer

class CarViewSet(viewsets.ModelViewSet):
    """Эндпоинт для работы с автомобилями"""
    queryset = Cars.objects.all()
    serializer_class = CarSerializer