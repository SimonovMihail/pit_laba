from rest_framework import serializers
from .models import Services, Masters, Orders, Clients, Boxes, Cars

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masters
        fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxes
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'