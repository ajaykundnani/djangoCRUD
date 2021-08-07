from django.core import validators
from django.forms import fields
from . models import User
from django  import forms

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','age','city','image']