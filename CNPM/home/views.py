from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse,HttpResponse
from .models import*
# Create your views here.
def error(request):
     return HttpResponse('ERROR 404')
def donate(request):
     fields = ('last-name','fisrt-name' ,'date','Email','phone','country','group-blood')
    
     if request.method=='POST' and 'sub_Inf' in request.POST:
     
          check = True
          DataDonate={'date':'2021-03-17'}
          for Oj in fields:
               if request.POST.get(Oj) == '':
                    check = False
                    print(Oj)
                    break;

               DataDonate[Oj]  = request.POST.get(Oj)

          if check == True:
               print(DataDonate)
               ins= GetProfileDonate(LastName =DataDonate['last-name'],FirstName =DataDonate['fisrt-name'],
               Date =DataDonate['date'],Email =DataDonate['Email'], Phone= DataDonate['phone'],
               Country = DataDonate['country'],TypeBlood = DataDonate['group-blood'])  
               ins.save()
          else:
                
               render(request,'home/homepage.html')
          # data = GetProfileDonate(DataDonate)
     # data.save()           
     return index(request)
def index(request):
    
     return TemplateResponse(request,'home/homepage.html')
def FeedBack(request):
     fields = ('ful-name' ,'Email','phone','your-message')

     if request.method=='POST' and 'Sub_FeedBack' in request.POST:
     
          check = True
          Data_Feedback={}
          for Oj in fields:
               if request.POST.get(Oj) == '':
                    check = False
                    print(Oj)
                    break;

               Data_Feedback[Oj]  = request.POST.get(Oj)
          if check == True:
               print(Data_Feedback)
               ins= FeedBacks(FullName =Data_Feedback['ful-name'],Email =Data_Feedback['Email'], Phone= Data_Feedback['phone'],Message= Data_Feedback['your-message'])  
               ins.save()
               
          else:
                
              index(request)
          # data = GetProfileDonate(DataDonate)
     # data.save()           
     return TemplateResponse(request,'home/homepage.html')

