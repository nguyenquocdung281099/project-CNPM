from django.urls import path
from CNPM import settings
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Manage'
urlpatterns = [ path('manage/', views.showTable, name='mange'),
              
]
