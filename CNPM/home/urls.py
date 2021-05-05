from django.urls import path
from CNPM import settings
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [ path('', views.donate, name='index'),
                path('donate/',views.donate,name='donate'),
                path('feedback/',views.FeedBack,name='feedback'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
