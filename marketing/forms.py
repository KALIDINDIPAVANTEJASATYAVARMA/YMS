from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from . import models

class MktgForm(forms.ModelForm):
    class Meta:
        model=models.mktg_master
        fields=['username','user_type','user_name','email_id','phone_no','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class customerform(forms.ModelForm):
    class Meta:
        model=models.customer_master
        fields=['customer_no','customer_name','customer_address','city','pin','phone_no','email_id']

class yard_form(forms.ModelForm):
    class Meta:
        model=models.yard_master
        fields=['yard_no']

class yard_receipt(forms.ModelForm):
    class Meta:
        model = models.yardreceipts
        fields = ['yard_no','receipt_id','transport_type','product_id','received_date','received_qty','remarks']

class yard_despatch(forms.ModelForm):
    class Meta:
        model = models.yard_despatchs
        fields = ['yard_no','despatch_id','transport_type','sale_order_id','despatch_date','despatched_qty','remarks']

class saleorder(forms.ModelForm):
    class Meta:
        model = models.sale_order
        fields = ['sale_order_id','customer_id','product_id','sale_order_date','sale_order_qty','remarks']





