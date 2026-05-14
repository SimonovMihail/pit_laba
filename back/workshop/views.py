from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils import timezone
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

@api_view(['POST'])
@permission_classes([AllowAny])
def public_order_create(request):
    # Получаем данные, которые пришли из FormData (scripts.js)
    name = request.data.get('name')
    phone = request.data.get('phone')
    comment = request.data.get('comment', '')

    if not name or not phone:
        return Response({'message': 'Заполните имя и телефон!'}, status=400)

    try:

        client, _ = Clients.objects.get_or_create(
            c_phone=phone,
            defaults={'c_fname': name, 'c_lname': 'Клиент с сайта'}
        )

        # Создаем "заглушку" для машины, так как заказ без машины не создастся
        car, _ = Cars.objects.get_or_create(
            c=client,
            car_brand="Заявка",
            car_model="С сайта",
            defaults={
                'car_plate': f"T-{phone[-4:]}",
                'car_info': comment
            }
        )

        # Создаем сам заказ
        # Поля: car, o_datetime, o_status из твоей модели Orders
        order = Orders.objects.create(
            car=car,
            o_datetime=timezone.now(),
            o_status='Новый'
        )

        return Response({
            'message': f'Спасибо, {name}! Заявка №{order.o_id} принята. Мы перезвоним.'
        }, status=201)

    except Exception as e:
        return Response({'message': f'Ошибка базы данных: {str(e)}'}, status=500)

def home_page(request):
    return render(request, 'page.html')