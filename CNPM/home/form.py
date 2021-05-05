from django import forms
from .models import GetProfileDonate

class ProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.LastName = kwargs.pop('last-name', None)
        self.FirstName = kwargs.pop('fisrt-name', None)
        self.Date = kwargs.pop('date', None)
        self.Email = kwargs.pop('Email', None)
        self.Phone = kwargs.pop('phone', None)
        self.Contry = kwargs.pop('contry', None)
        self.Typeblood = kwargs.pop('group-blood', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        Profile = super().save(commit=False)
        Profile.LastName = self.pop('LastName', None)
        Profile.FirstName = self.pop('FirstName', None)
        Profile.Date = self.pop('Date', None)
        Profile.Email = self.pop('Email', None)
        Profile.Phone = self.pop('Phone', None)
        Profile.Contry = self.pop('Contry', None)
        Profile.Typeblood = self.pop('group-blood', None)
        Profile.save()
    class Meta:
        model = GetProfileDonate
        fields = ('LastName','FirstName' ,'Date','Email','Phone','Contry','TypeBlood')