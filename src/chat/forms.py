from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Room

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']


class RoomCreationsForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'private_room', 'passcode']
