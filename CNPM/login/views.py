from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse,HttpResponse
from .models import *
from home.views import index
# Create your views here.
def login(request):

    if request.method =="POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      user = {username:password}
      
      if user is not None:
            data = checkLogin.objects.all()
            arr_auth={}
            for i in data:
                arr_auth[i.username]=i.password
            
            try:
                if arr_auth.get(username)==password:
                    return index(request)
                else:
                 return TemplateResponse(request,'login/index.html')
            except:
                pass

    return TemplateResponse(request,'login/index.html')
