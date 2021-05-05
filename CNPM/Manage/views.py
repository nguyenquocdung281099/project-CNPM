from django.shortcuts import render
from home.models import GetProfileDonate
from django.http import HttpResponse,HttpRequest
# Create your views here.
def showTable(request):
    Objs = GetProfileDonate.objects.all()
    print(len(Objs))
    customer_list = {'obj_records':Objs}
    return  render(request,'Manage/Admin_Manage.html',context=customer_list)
