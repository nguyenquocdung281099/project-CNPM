from django.contrib import admin
from .models import GetProfileDonate,FeedBacks
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    title = 'List person donate'
    list_display = ('FirstName','LastName','Date','Email','Phone','Country','TypeBlood')
admin.site.register(GetProfileDonate,AuthorAdmin)
class AuthorFeedBack(admin.ModelAdmin):
    title = 'List FeedBack'
    list_display = ('FullName','Email','Phone','Message')
admin.site.register(FeedBacks,AuthorFeedBack)
