from django import forms
from .models import Booking

class Contact(forms.Form):
    """ Contact Form from FiveStars Car Service"""
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=20, required=True)
    message = forms.CharField(max_length=200, required=True)
    cc_myself = forms.BooleanField(required=False)
    

class Booking(forms.Form):
    pick_up = forms.CharField(max_length=50)
    destiny = forms.CharField(max_length=50)
    full_name = forms.CharField(max_length=50)
    email= forms.EmailField()
    flight = forms.CharField(max_length=20)
    date = forms.DateField()
    date_time = forms.CharField(max_length=50)
    payment_method = forms.CharField(max_length=12)
    type_of_travel = forms.CharField(max_length=12)                  
    observations = forms.CharField(max_length=100)
    passengers = forms.IntegerField()
    class Meta:
        model = Booking
        fields = ['pick_up','destiny','full_name','full_name','email','flight','date','date_time','payment_method','type_of_travel','observations','passengers']