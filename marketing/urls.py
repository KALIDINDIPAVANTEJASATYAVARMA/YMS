"""yms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from django.contrib.admin import autodiscover
from marketing import views

autodiscover()

urlpatterns = [
    path('marketingclick', views.mrktclick_view),
    path('mrktsignup', views.mrkt_signup_view,name='mrktsignup'),
    path('mrktlogin', views.mrkt_login_view,name='mrktlogin'),
    path('mrkt-dashboard', views.mrkt_dashboard_view,name='mrkt-dashboard'),
    path('logout',views.mrkt_logout_view,name='mrktlogout'),
    path('mrktmaster',views.mrktmaster,name='mrktmaster'),
    path('adminmaster',views.adminmaster,name='adminmaster'),
    path('customer',views.customer,name='customer'),
    path('addcustomer',views.addcustomer,name='addcustomer'),
    path('viewcustomer',views.viewcustomer,name='viewcustomer'),
    path('yard',views.yard,name='yard'),
    path('addyard',views.addyard,name='addyard'),
    path('viewyard',views.viewyard,name='viewyard'),
    path('receipt',views.receipt,name='receipt'),
    path('yardreceipt',views.yardreceipt,name='yardreceipt'),
    path('yarddespatch',views.yarddespatch,name='yarddespatch'),
    path('saleorder',views.saleorder1,name='saleorder1'),
    path('addsaleorder',views.addsaleorder,name='addsaleorder'),
    path('viewsaleorder',views.viewsaleorder,name='viewsaleorder'),
    path('yard_receipt_1/<int:yard_no>',views.yard_receipt_1,name='yard_receipt_1'),
    path('yard_despatch_1/<int:yard_no>',views.yard_despatch_1,name='yard_despatch_1')
]