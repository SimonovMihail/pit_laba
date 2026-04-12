from django.db import models

class Administrators(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100, blank=True, null=True)
    admin_phone = models.CharField(max_length=15, blank=True, null=True)
    admin_email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'administrators'


class Boxes(models.Model):
    b_id = models.AutoField(primary_key=True)
    b_number = models.IntegerField()
    b_capacity = models.IntegerField(blank=True, null=True)
    b_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'boxes'


class Cars(models.Model):
    car_id = models.AutoField(primary_key=True)
    c = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_year = models.IntegerField(blank=True, null=True)
    car_packet = models.CharField(max_length=100, blank=True, null=True)
    car_info = models.TextField(blank=True, null=True)
    car_plate = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cars'

    def __str__(self):
        return f"{self.car_brand} {self.car_model} ({self.car_plate})"


class Clients(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_lname = models.CharField(max_length=50)
    c_fname = models.CharField(max_length=50)
    c_sname = models.CharField(max_length=50, blank=True, null=True)
    c_age = models.IntegerField(blank=True, null=True)
    c_gender = models.CharField(max_length=1, blank=True, null=True)
    c_phone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    c_email = models.CharField(max_length=50, blank=True, null=True)
    c_visits = models.IntegerField(blank=True, null=True)
    c_discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clients'

    def __str__(self):
        return f"{self.c_lname} {self.c_fname} {self.c_sname}"


class Masters(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=100)
    m_spec = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'masters'

    def __str__(self):
        return self.m_name


class OrderDetails(models.Model):
    id = models.IntegerField(primary_key=True)


    o = models.ForeignKey('Orders', models.DO_NOTHING)
    s = models.ForeignKey('Services', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'order_details'
        unique_together = (('o', 's'),)

class Orders(models.Model):
    o_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(Masters, models.DO_NOTHING, blank=True, null=True)
    b = models.ForeignKey(Boxes, models.DO_NOTHING, blank=True, null=True)
    o_datetime = models.DateTimeField()
    o_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orders'


class Services(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100, blank=True, null=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'services'

    def __str__(self):
        return self.s_name