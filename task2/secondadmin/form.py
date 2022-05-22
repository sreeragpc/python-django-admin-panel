from django import forms

class UserdataForm(forms.Form):
    username=forms.CharField(label='name',max_length=254)
    password=forms.CharField(label='password',max_length=16 ,widget=forms.PasswordInput())
