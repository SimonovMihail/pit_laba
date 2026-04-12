from django.contrib import admin
from .models import Clients, Cars, Masters, Boxes, Services, Orders, Administrators

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('c_lname', 'c_fname', 'c_phone', 'c_visits')
    search_fields = ('c_lname', 'c_phone')

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'car_plate', 'c')

@admin.register(Masters)
class MastersAdmin(admin.ModelAdmin):
    list_display = ('m_name', 'm_spec')

@admin.register(Boxes)
class BoxesAdmin(admin.ModelAdmin):
    list_display = ('b_number', 'b_status', 'b_capacity')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('s_name', 'base_price')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('o_id', 'car', 'm', 'o_status', 'o_datetime')
    list_filter = ('o_status',)

admin.site.register(Administrators)