from django import forms
from django.contrib.auth.models import User
from . import models

class AdminForm(forms.ModelForm):
    class Meta:
        model=models.admin_master
        fields=['username','user_type','user_name','email_id','phone_no','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())       

class productform(forms.ModelForm):
    class Meta:
        model=models.product_master
        fields=['product_id','product_desc','stock_in_tons','location','product_grade']

class transportform(forms.ModelForm):
    class Meta:
        model=models.transport_master
        fields=['driver_id','vehicle_type','driver_name','email_id','phone_no']
 