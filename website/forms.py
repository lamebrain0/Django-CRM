from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email Address'}))
    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}))
    
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password1','password2')
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        