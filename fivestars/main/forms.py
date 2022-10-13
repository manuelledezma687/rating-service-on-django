from django import forms


class Contact(forms.Form):
    """ Contact Form from FiveStars Car Service"""
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=20, required=True)
    message = forms.CharField(max_length=200, required=True)