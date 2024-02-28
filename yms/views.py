from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.

def home_view(request):
    return render(request,'index.html')

 