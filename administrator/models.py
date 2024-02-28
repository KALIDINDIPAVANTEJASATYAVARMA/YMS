from django.db import models

# Create your models here.

class admin_master(models.Model):
    username = models.CharField(max_length=6,primary_key=True)
    user_type = models.CharField(max_length=13,default='administrator')
    user_name = models.CharField(max_length=40,default='a',null=False)
    email_id = models.CharField(max_length=20,default=0)
    phone_no = models.CharField(max_length=10,default=0000000000) 
    password = models.CharField(max_length=20,default='12345678')

    @property
    def get_instance(self):
        return self

class product_master(models.Model):
    product_id = models.CharField(max_length=6,primary_key=True)
    product_desc = models.CharField(max_length=40,default='steel')
    stock_in_tons = models.IntegerField(default=0)
    location = models.CharField(max_length=20,default='furnace')
    product_grade = models.CharField(max_length=10,default='a')

    def __str__(self):
        return str(self.pk)
    
class transport_master(models.Model):
    driver_id = models.CharField(max_length=6,primary_key=True)
    vehicle_type = models.CharField(max_length=5,default='truck')
    driver_name = models.CharField(max_length=40,default='xyz',null=False)
    email_id = models.CharField(max_length=20,default=0)
    phone_no = models.CharField(max_length=10,default=0000000000) 

    def __str__(self):
        return str(self.pk)