from pyexpat import model
from time import timezone
from django.db import models
from administrator.models import product_master

# Create your models here.

class mktg_master(models.Model):
    username = models.CharField(max_length=6,primary_key=True)
    user_type = models.CharField(max_length=13,default='marketing')
    user_name = models.CharField(max_length=40,default='a',null=False)
    email_id = models.CharField(max_length=20,default=0)
    phone_no = models.CharField(max_length=10,default=0000000000) 
    password = models.CharField(max_length=20,default='12345678')

    @property
    def get_instance(self):
        return self
    
class customer_master(models.Model):
    customer_no = models.CharField(max_length=6,primary_key=True)
    customer_name = models.CharField(max_length=40,default='pavan')
    customer_address = models.CharField(max_length=40,default='ukkunagaram')
    city = models.CharField(max_length=20,default='vizag')
    pin = models.IntegerField(default=530032)
    phone_no = models.IntegerField(default=0000000000)
    email_id = models.CharField(max_length=30,default="abc@gmail.com")

    def __str__(self):
        return str(self.pk)

class yard_master(models.Model):
    yard_no = models.IntegerField(primary_key=True,default=0)

    def __str__(self):
        return str(self.pk)

class yardreceipts(models.Model):
    yard_no = models.ForeignKey(yard_master,on_delete=models.CASCADE)
    receipt_id = models.IntegerField(default=000000,primary_key=True)
    transport_type = models.CharField(max_length=10,default='truck')
    product_id = models.ForeignKey(product_master,on_delete=models.CASCADE,unique=True,default='000000')
    received_date = models.CharField(max_length=10,default='21-06-2023')
    received_qty = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=60,default='good')

class sale_order(models.Model):
    sale_order_id = models.IntegerField(default=000000,primary_key=True)
    customer_id = models.ForeignKey(customer_master,on_delete=models.CASCADE,unique=True,default='000000')
    product_id = models.ForeignKey(product_master,on_delete=models.CASCADE,unique=True,default='000000')
    sale_order_date = models.CharField(max_length=10,default='21-06-2023')
    sale_order_qty = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=60,default='good')


class yard_despatchs(models.Model):
    yard_no = models.ForeignKey(yard_master,on_delete=models.CASCADE)
    despatch_id = models.IntegerField(default=000000,primary_key=True)
    transport_type = models.CharField(max_length=10,default='truck')
    sale_order_id = models.ForeignKey(sale_order,on_delete=models.CASCADE,unique=True,default='000000')
    despatch_date = models.CharField(max_length=10,default='21-06-2023')
    despatched_qty = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=60,default='good')
    


