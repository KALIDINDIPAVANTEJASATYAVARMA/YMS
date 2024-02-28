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
from administrator import views

autodiscover()

urlpatterns = [
    path('adminclick', views.adminclick_view),
    path('adminsignup', views.admin_signup_view,name='adminsignup'),
    path('adminlogin', views.admin_login_view,name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('logout',views.admin_logout_view,name='adminlogout'),
    path('mrktmaster',views.mrktmaster,name='mrktmaster'),
    path('adminmaster',views.adminmaster,name='adminmaster'),
    path('product',views.product,name='product'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('yard',views.yard,name='yard'),
    path('viewyard',views.viewyard,name='viewyard'),
    path('transport',views.transport,name='transport'),
    path('addtransport',views.addtransport,name='addtransport'),
    path('viewtransport',views.viewtransport,name='viewtransport')
]