from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from . import forms,models
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import LoginForm,productform,transportform
from .models import admin_master,product_master,transport_master
from marketing.models import mktg_master,yard_master

# Create your views here.



def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'adminclick.html')

def admin_signup_view(request):
    AdminForm=forms.AdminForm()
    mydict={'AdminForm':AdminForm}
    if request.method=='POST':
        AdminForm=forms.AdminForm(request.POST,request.FILES)
        if AdminForm.is_valid():
            user=AdminForm.save()
            user.save()   
            my_admin_group = Group.objects.get_or_create(name='admin')
            my_admin_group[0].user_set.add(user)         
        return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html',context=mydict)

def is_admin(user):
    return user.groups.filter(name='admin').exists()

def admin_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = admin_master.objects.get(username=username, password=password)
                # User authentication successful, perform login
                request.session['username'] = user.username
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('admin-dashboard')
            except admin_master.DoesNotExist:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()
        error_message = None

    context = {
        'form': form,
        'error_message': error_message,
        'next_url': reverse('admin-dashboard')  # Pass the URL name of mrkt-dashboard view as the next_url
    }
    return render(request, 'adminlogin.html',context)

def admin_dashboard_view(request):
    return render(request,'admin_dashboard.html')

def admin_logout_view(request):
    return render(request,'adminclick.html')

def mrktmaster(request):
    data = mktg_master.objects.all()
    context = {'data':data}
    return render(request,'mrktmaster1.html',context)

def adminmaster(request):
    data = admin_master.objects.all()
    context = {'data':data}
    return render(request,'adminmaster1.html',context)

def product(request):
    return render(request,'product.html')

def viewproduct(request):
    data = product_master.objects.all()
    context = {'data':data}
    return render(request,'viewproduct.html',context)

def addproduct(request):
    productform = forms.productform()
    if request.method=='POST':
        productform = forms.productform(request.POST)
        if productform.is_valid():        
            productform.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('viewproduct')
    return render(request,'addproduct.html',{'productform':productform})

def yard(request):
    return render(request,'yard1.html')

def viewyard(request):
    data = yard_master.objects.all()
    context = {'data':data}
    return render(request,'viewyard1.html',context)

def transport(request):
    return render(request,'transport.html')

def viewtransport(request):
    data = transport_master.objects.all()
    context = {'data':data}
    return render(request,'viewtransport.html',context)

def addtransport(request):
    transportform = forms.transportform()
    if request.method=='POST':
        transportform = forms.transportform(request.POST)
        if transportform.is_valid():        
            transportform.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('viewtransport')
    return render(request,'addtransport.html',{'transportform':transportform})


