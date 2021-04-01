from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
# from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
# from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','password1','password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'name', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'id': 'name', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'id': 'name', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Your Email'}),
            'password1': forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'id': 're_pass', 'placeholder': 'Confirm Password'}),

        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']