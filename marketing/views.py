from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import LoginForm,customerform,yard_form,yard_receipt,yard_despatch,saleorder
from .models import mktg_master,customer_master,yard_master,sale_order,yardreceipts,yard_despatchs
from administrator.models import admin_master


# Create your views here.



def mrktclick_view(request):  
    return render(request,'mrktclick.html') 

def mrkt_signup_view(request):
    MktgForm=forms.MktgForm()
    mydict={'MktgForm':MktgForm}
    if request.method=='POST':
        MktgForm=forms.MktgForm(request.POST,request.FILES)
        if MktgForm.is_valid():
            user=MktgForm.save()
            user.save()   
            my_mrkt_group = Group.objects.get_or_create(name='marketing')
            my_mrkt_group[0].user_set.add(user)         
        return HttpResponseRedirect('mrktlogin')
    return render(request,'mrktsignup.html',context=mydict)

def mrkt_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = mktg_master.objects.get(username=username, password=password)
                # User authentication successful, perform login
                request.session['username'] = user.username
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('mrkt-dashboard')
            except mktg_master.DoesNotExist:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()
        error_message = None

    context = {
        'form': form,
        'error_message': error_message,
        'next_url': reverse('mrkt-dashboard')  # Pass the URL name of mrkt-dashboard view as the next_url
    }
    return render(request, 'mrktlogin.html',context)


def is_mrkt(user):
    return user.groups.filter(name='marketing').exists()

def mrkt_dashboard_view(request):
    return render(request,'mrkt_dashboard.html')

def mrkt_logout_view(request):
    return render(request,'mrktclick.html')

def mrktmaster(request):
    data = mktg_master.objects.all()
    context = {'data':data}
    return render(request,'mrktmaster.html',context)

def adminmaster(request):
    data = admin_master.objects.all()
    context = {'data':data}
    return render(request,'adminmaster.html',context)

def customer(request):
    return render(request,'customer.html')

def viewcustomer(request):
    data = customer_master.objects.all()
    context = {'data':data}
    return render(request,'viewcustomer.html',context)

def addcustomer(request):
    customerform = forms.customerform()
    if request.method=='POST':
        customerform = forms.customerform(request.POST)
        if customerform.is_valid():        
            customerform.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('marketing/viewcustomer')
    return render(request,'addcustomer.html',{'customerform':customerform})

def yard(request):
    return render(request,'yard.html')

def addyard(request):
    yard_form=forms.yard_form()
    if request.method=='POST':
        yard_form=forms.yard_form(request.POST)
        if yard_form.is_valid():
            yard_form.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('viewyard')
    return render(request,'addyard.html',{'yard_form':yard_form})

def viewyard(request):
    data = yard_master.objects.all()
    context = {'data':data}
    return render(request,'viewyard.html',context)

def receipt(request):
    return render(request,'receipt.html')

def yardreceipt(request):
    yard_receipt=forms.yard_receipt()
    if request.method=='POST':
        yard_receipt=forms.yard_receipt(request.POST)
        if yard_receipt.is_valid():
            yard_receipt.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('receipt')
    return render(request,'yardreceipt.html',{'yard_receipt':yard_receipt})

def yarddespatch(request):
    yard_despatch=forms.yard_despatch()
    if request.method=='POST':
        yard_despatch=forms.yard_despatch(request.POST)
        if yard_despatch.is_valid():
            yard_despatch.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('receipt')
    return render(request,'yarddespatch.html',{'yard_despatch':yard_despatch})

def saleorder1(request):
    return render(request,'saleorder.html')

def addsaleorder(request):
    saleorder=forms.saleorder()
    if request.method=='POST':
        saleorder=forms.saleorder(request.POST)
        if saleorder.is_valid():
            saleorder.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('viewsaleorder')
    return render(request,'addsaleorder.html',{'saleorder':saleorder})

def viewsaleorder(request):
    data = sale_order.objects.all()
    context = {'data':data}
    return render(request,'viewsaleorder.html',context)

def yard_receipt_1(request,yard_no):
    data = yardreceipts.objects.filter(yard_no=yard_no)
    context = {'data':data}
    return render(request,'yard_receipt_1.html',context)

def yard_despatch_1(request,yard_no):
    data = yard_despatchs.objects.filter(yard_no=yard_no)
    context = {'data':data}
    return render(request,'yard_despatch_1.html',context)


    

        



    



